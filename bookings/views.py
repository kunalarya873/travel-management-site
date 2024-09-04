from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import TravelOption, Booking
from .forms import BookingForm
from django.contrib import messages



def home(request):
    if request.user.is_authenticated:
        return redirect('profile')  # Redirect authenticated users to the profile page
    else:
        return redirect('login') 
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get user data
            user = form.get_user()
            # Log the user in
            login(request, user)
            # Redirect to a success page
            messages.success(request, "You are now logged in.")
            return redirect('profile')  # Redirect to home or another page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page or any other page
    else:
        return redirect('login')  # Redirect to login page if accessed via GET


@login_required
def travel_options(request):
    options = TravelOption.objects.all()
    return render(request, 'travel_options.html', {'options': options})

@login_required
def book(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            number_of_seats = form.cleaned_data['number_of_seats']
            total_price = travel_option.price * number_of_seats
            Booking.objects.create(
                user=request.user,
                travel_option=travel_option,
                number_of_seats=number_of_seats,
                total_price=total_price
            )
            return redirect('my_bookings')
    else:
        form = BookingForm()
    context = {
        'travel_option': travel_option,
        'form': form
    }
    return render(request, 'book_travel.html', context)

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    if booking.user == request.user:
        booking.status = 'Cancelled'
        booking.save()
    return redirect('my_bookings')
