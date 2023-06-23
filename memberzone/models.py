from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import timedelta, date
from django.utils import timezone

# Create your models here.
TIME_SLOTS = []

hours = ['08:', '09:', '10:', '11:', '12:', '13:', '14:', '15:', '16:', '17:']
slots = ['00', '15', '30', '45']

for hour in hours:
    for slot in slots:
        time = "".join([hour, slot])
        TIME_SLOTS.append((time, time))


def next_day():
    return date.today() + timedelta(days=1)


class BookingDate(models.Model):

    booking_date = models.DateField(default=next_day,
                                    validators=[MinValueValidator(next_day)],
                                    null=False, blank=False)


class BookingTimes(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(default=next_day,
                                    validators=[MinValueValidator(next_day)],
                                    null=False, blank=False)
    booking_time = models.CharField(
        choices=TIME_SLOTS, blank=False, max_length=5)
    created_on = models.DateTimeField(auto_now_add=True)
    number_players = models.IntegerField(blank=False,
                                         default=1,
                                         validators=[
                                             MaxValueValidator(4),
                                             MinValueValidator(1)
                                         ]
                                         )

    def __str__(self):
        return f"{self.booking_time}"

    objects = models.Manager()
