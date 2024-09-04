# Travel Booking Application

## Overview

Welcome to the Travel Booking Application! This project is a simple web-based application developed using Python's Django framework. It allows users to view available travel options, book tickets, and manage their bookings. The frontend is built using Django templates, and the application is styled for both usability and responsiveness.

## Features

### Backend

1. **User Management**
   - User registration, login, and logout using Django's built-in authentication system.
   - Users can update their profile information.

2. **Travel Options**
   - Models to represent different travel options such as flights, trains, and buses.
   - Key fields include: Travel ID, Type, Source, Destination, Date and Time, Price, and Available Seats.

3. **Booking**
   - Users can book travel options by selecting a travel option, entering details, and confirming the booking.
   - Booking model includes: Booking ID, User (Foreign Key), Travel Option (Foreign Key), Number of Seats, Total Price, Booking Date, and Status (Confirmed, Cancelled).

4. **View and Manage Bookings**
   - Users can view their current and past bookings.
   - Functionality to cancel bookings.

### Frontend

1. **User Interface**
   - Simple, user-friendly pages designed using Django templates.
   - Views for user registration, login, profile management, listing available travel options, booking form, and displaying bookings.

2. **Responsiveness**
   - Pages are designed to be functional across various devices (desktop, mobile).

3. **Styling**
   - Styled with CSS and optional use of Bootstrap for rapid development.

## Setup Instructions

To set up and run this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kunalarya873/travel-management-site.git
   cd travel-booking-app
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - The project is set up to use SQLite3 by default. To switch to MySQL, modify the `DATABASES` setting in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```
   - Ensure you have MySQL installed and the `mysqlclient` package is added to `requirements.txt`.

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional for Admin Access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Bonus Features

- **Database**: Although SQLite3 is used by default, you can configure the project to use MySQL.
- **Cloud Deployment**: Deployment to AWS or another cloud platform is recommended but not included by default.
- **Validation**: Basic validation is implemented for user input and available seats.
- **Unit Tests**: Basic unit tests are included for critical features.
- **Search and Filtering**: Enhanced search and filtering capabilities for travel options.

## Deployment

If deployed, you can access the application at the following URL:
[Your Deployed Application URL]

## Repository

The source code is available on GitHub:
[https://github.com/kunalarya873/travel-management-site.git](https://github.com/kunalarya873/travel-management-site.git)
