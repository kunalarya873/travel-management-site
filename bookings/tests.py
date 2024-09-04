from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking

class BookingTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.travel_option = TravelOption.objects.create(
            travel_type='Flight',
            source='New York',
            destination='Los Angeles',
            date_time='2024-10-10 10:00:00',
            price=100.00,
            available_seats=10
        )

    def test_booking(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(f'/book/{self.travel_option.travel_id}/', {'number_of_seats': 2})
        self.assertEqual(response.status_code, 302)  # Check redirection after booking
        self.assertEqual(Booking.objects.count(), 1)
