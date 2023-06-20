from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import MakeBooking

# Create your views here.


def booking(request):
    if request.method == "POST":
        form = MakeBooking(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            messages.success(request, ("Booking Successful!"))
            return redirect('booking')
    else:
        form = MakeBooking()

    return render(request, 'memberzone/booking.html', {'form': form})
