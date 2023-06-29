from django.test import TestCase
from memberzone.models import BookingTimes
from django.contrib.auth.models import User

# Create your tests here.


class BookingTimesTest(TestCase):

    """ Test booking times model """

    def setUp(self):
        """ set up test data and user """

        user = User.objects.create(username='testuser',
                                   email="test@testemail.com",
                                   first_name="test1st", last_name="testlast",
                                   password='12345')

        BookingTimes.objects.create(owner=user,
                                    booking_date="2023-06-30",
                                    booking_time="10:00",
                                    created_on="June 29, 2023, 6:36 p.m.",
                                    number_players="2")

    def test_record_created(self):
        """ test record created """

        self.assertTrue(BookingTimes.objects.get(
            pk=1))
