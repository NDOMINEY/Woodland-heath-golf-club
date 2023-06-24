from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from . forms import MakeBooking, SelectBookingDate
from . models import BookingTimes
import json


# Create your views here.


def select_bookingdate(request):
    if request.method == "POST":
        form = SelectBookingDate(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['booking_date']
            str_date = selected_date.strftime("%Y-%m-%d")
            request.session['booking_date'] = str_date
            return redirect('booking')
    else:
        form = SelectBookingDate()

    return render(request, 'memberzone/select_bookingdate.html',
                  {'form': form})


def booking(request):

    if request.method == "POST":
        form = MakeBooking(request.POST)
        if form.is_valid():
            booking_date = request.session['booking_date']
            form.instance.owner = request.user
            form.instance.booking_date = booking_date
            form.save()
            messages.success(request, ("Booking Successful!"))
            return redirect('home')
    else:
        form = MakeBooking()

    booking_date = request.session['booking_date']

    date_formatting = datetime.strptime(booking_date, '%Y-%m-%d')

    booked_date = date_formatting.strftime("%d-%m-%Y")

    pull_booked_slots = BookingTimes.objects.filter(
        booking_date=booking_date).values('booking_time')
    booked_slots = list(pull_booked_slots)
    print(booked_slots)

    return render(request,
                  'memberzone/booking.html', {'form': form,
                                              'booked_slots':
                                              json.dumps(booked_slots),
                                              "booked_date": booked_date})
