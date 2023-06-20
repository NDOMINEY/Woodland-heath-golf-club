from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
TIME_SLOTS = []

hours = ['08:', '09:', '10:', '11:', '12:', '13:', '14:', '15:', '16:', '17:']
slots = ['00', '15', '30', '45']

for hour in hours:
    for slot in slots:
        time = "".join([hour, slot])
        TIME_SLOTS.append((time, time))


class BookingTimes(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(
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
