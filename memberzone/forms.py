from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . models import BookingTimes


class MakeBooking(ModelForm):

    class Meta:
        model = BookingTimes
        fields = ('owner', 'booking_date', 'booking_time',
                  'number_players')
        widgets = {
            'booking_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
