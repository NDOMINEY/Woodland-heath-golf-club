from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . models import BookingTimes, BookingDate


class SelectBookingDate(ModelForm):

    class Meta:
        model = BookingDate
        fields = ('booking_date',)
        widgets = {
            'booking_date': forms.widgets.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
        }


class MakeBooking(ModelForm):

    class Meta:
        model = BookingTimes
        fields = ('booking_time',
                  'number_players')
        widgets = {
            'booking_date': forms.widgets.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'booking_time': forms.widgets.RadioSelect(
                attrs={'class': 'hidden-radio'}),
        }

    def __init__(self, *args, **kwargs):
        super(MakeBooking, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field, forms.TypedChoiceField):
                field.choices = field.choices[1:]


class ChangeBooking(ModelForm):

    class Meta:
        model = BookingTimes
        fields = ('number_players',)

    def __init__(self, *args, **kwargs):
        super(ChangeBooking, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field, forms.TypedChoiceField):
                field.choices = field.choices[1:]
