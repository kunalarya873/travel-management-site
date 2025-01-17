from django.db import models
from django.contrib.auth.models import User

class TravelOption(models.Model):
    TRAVEL_TYPE_CHOICES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]
    
    travel_id = models.AutoField(primary_key=True)
    travel_type = models.CharField(max_length=10, choices=TRAVEL_TYPE_CHOICES, default='Flight')
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.travel_type} from {self.source} to {self.destination} on {self.date_time}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')
    
    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username} for {self.travel_option}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    
    # Add more fields here if necessary

    def __str__(self):
        return self.user.username
