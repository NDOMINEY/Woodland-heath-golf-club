from django.urls import path
from . views import booking, select_bookingdate, memberzone, view_bookings, delete_bookings

urlpatterns = [
    path('booking/', booking, name='booking'),
    path('selectbookingdate/', select_bookingdate, name='booking_date'),
    path('memberzone/', memberzone, name='memberzone'),
    path('memberzone/view_bookings/', view_bookings, name='view_bookings'),
    path('memberzone/view_bookings/delete_bookings/<booking_id>',
         delete_bookings, name="delete_bookings")
]
