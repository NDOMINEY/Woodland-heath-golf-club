from django.urls import path
from . views import booking, select_bookingdate

urlpatterns = [
    path('booking/', booking, name='booking'),
    path('selectbookingdate/', select_bookingdate, name='booking_date'),
]
