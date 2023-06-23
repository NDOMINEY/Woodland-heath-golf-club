from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from . forms import MakeBooking, SelectBookingDate
from . models import BookingTimes

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
            form.instance.owner = request.user
            form.save()
            messages.success(request, ("Booking Successful!"))
            return redirect('booking')
    else:
        form = MakeBooking(request)

    booking_date = request.session['booking_date']

    pull_booked_slots = BookingTimes.objects.filter(
        booking_date=booking_date)
    booked_slots = list(pull_booked_slots)
    print(booked_slots)

    return render(request,
                  'memberzone/booking.html', {'form': form,
                                              'booked_slots': booked_slots})
