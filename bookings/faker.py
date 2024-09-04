from .models import TravelOption, Booking, Profile
from faker import Faker
from random import randint, choice
from django.contrib.auth.models import User
from django.utils import timezone

fake = Faker()

def create_travel_options():
    for _ in range(100):
        TravelOption.objects.create(
            price=round(randint(10, 100) + randint(0, 99) / 100, 2),  # Ensure decimal format
            destination=fake.city(),
            source=fake.city(),
            available_seats=randint(0, 100),
            date_time=fake.date_time_this_decade()
        )
    return TravelOption.objects.all()

def create_users():
    for _ in range(100):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()  # Ensure this is a valid password

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        except Exception as e:
            print(f"Error creating user: {username}, {email}, {password} - {e}")

    return User.objects.all()

def create_bookings():
    users = list(User.objects.all())
    travel_options = list(TravelOption.objects.all())
    if not users:
        raise ValueError("No users available to assign to bookings")
    if not travel_options:
        raise ValueError("No travel options available to book")
        
    for _ in range(100):
        Booking.objects.create(
            user=choice(users),  # Ensure a valid user is assigned
            travel_option=choice(travel_options),  # Ensure a valid travel option is assigned
            number_of_seats=randint(1, 10),
            total_price=round(randint(10, 100) + randint(0, 99) / 100, 2),
            status=choice(['Confirmed', 'Cancelled']),
            booking_date=fake.date_time_this_decade()
        )
    return Booking.objects.all()

def create_profiles():
    users = User.objects.all()
    for user in users:
        # Check if a profile already exists for this user
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(
                user=user,
                username=user.username,  # Should be consistent with User model
                email=user.email,  # Should be consistent with User model
                password=user.password,  # Not used directly
                phone_number=fake.phone_number(),
                address=fake.address()
            )
    return Profile.objects.all()

def clear_existing_profiles():
    Profile.objects.all().delete()
