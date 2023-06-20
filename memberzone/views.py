from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import BookingTimes

# Create your views here.

def booking(request):
    if request.method == "POST":
        form = BookingTimes(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Booking Successful!"))
            return redirect('booking')
    else:
        form = BookingTimes()

    return render(request, 'memberzone/booking.html', {'form': form})
