from django.contrib import admin
from . models import BookingTimes

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ("owner", "created_on", "booking_date",
                    "booking_time", "number_players")



admin.site.register(BookingTimes, BookingAdmin)
