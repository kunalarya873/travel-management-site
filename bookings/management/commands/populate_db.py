from django.core.management.base import BaseCommand
from bookings.faker import create_travel_options, create_users, create_bookings, create_profiles

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        create_travel_options()
        create_users()
        create_bookings()
        create_profiles()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
