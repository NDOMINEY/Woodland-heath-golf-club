from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . models import BookingTimes


class MakeBooking(ModelForm):

    class Meta:
        model = BookingTimes
        fields = ('booking_date', 'booking_time',
                  'number_players')
        widgets = {
            'booking_date': forms.widgets.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'booking_time': forms.widgets.RadioSelect(
                attrs={'class': 'hidden-radio'}),
        }

    def __init__(self, *args, **kwargs):
        super(MakeBooking, self).__init__(*args, **kwargs)

        time_slots = ['08:00', '08:15', '08:30', '08:45',
                      '09:00', '09:15', '09:30', '09:45',
                      '10:00', '10:15', '10:30', '10:45',
                      '11:00', '11:15', '11:30', '11:45',
                      '12:00', '12:15', '12:30', '12:45',
                      '13:00', '13:15', '13:30', '13:45',
                      '14:00', '14:15', '14:30', '14:45',
                      '15:00', '15:15', '15:30', '15:45',
                      '16:00', '16:15', '16:30', '16:45',
                      '17:00', '17:15', '17:30', '17:45',]

        pull_booked_slots = BookingTimes.objects.filter(
            booking_date='2023-06-24')
        booked_slots = list(pull_booked_slots)
        available_slots = []

        print(time_slots)
        print(booked_slots)

        for slot in booked_slots:
            print(slot)
            if slot in time_slots:
                time_slots.remove(slot)
                print(time_slots)
        

        for slot in time_slots:
            available_slots.append((slot, slot))

        # for time in time_slots:
        #     if time not in booked_slots:
        #         available_slots.append((time, time))

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field, forms.TypedChoiceField):
                field.choices = available_slots
