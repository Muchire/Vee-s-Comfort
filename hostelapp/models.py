import random
from django.db import models
from django.contrib.auth.models import User
class Hostel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hostel_images/')
    location = models.CharField(max_length=100)
    room_number = models.IntegerField()
    breakfast_menu = models.ImageField(upload_to='hostel_menus/', null=True, blank=True)
    lunch_menu = models.ImageField(upload_to='hostel_menus/', null=True,)

    def __str__(self):
        return self.name

class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hostel_images/')

class Meal(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meal_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, blank=True, editable=False)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    include_breakfast = models.BooleanField(default=False)
    include_lunch = models.BooleanField(default=False)
    airport_pickup_option = models.BooleanField(default=False)
    flight_number = models.CharField(max_length=20, null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    CAR_CHOICES = [
        ('Taxi', 'Taxi'),
        ('Van', 'Van'),
    ]
    car_type = models.CharField(max_length=10, choices=CAR_CHOICES, null=True, blank=True)
    room_service = models.BooleanField(default=False)  # New field for room service

    def save(self, *args, **kwargs):
        if not self.room_number:
            self.room_number = str(random.randint(1000, 9999))
        
        # Calculate total price
        num_nights = (self.check_out - self.check_in).days
        self.total_price = self.hostel.price_per_night * num_nights
        if self.include_breakfast:
            self.total_price += 500 * num_nights
        if self.include_lunch:
            self.total_price += 500 * num_nights
        
        # Add airport pickup charges
        if self.airport_pickup_option:
            if self.car_type == 'Taxi':
                self.total_price += 500
            elif self.car_type == 'Van':
                self.total_price += 800
        
        # Add room service charges
        if self.room_service:
            self.total_price += 500
        
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.room_number} by {self.user}"


class AirportPickup(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='airport_pickup')
    pickup_time = models.DateTimeField()
    flight_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class MealService(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='meal_services')
    meal_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    served_date = models.DateField()


class TourGuideService(models.Model):  # New Model for Tour Guide
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tour_guide_services')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Added user field
    guide_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_date = models.DateField()

    def __str__(self):
        return f"Tour Guide Service by {self.user} with {self.guide_name} on {self.tour_date}"
    

class Payment(models.Model): 
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_method = models.CharField(max_length=50, choices=[('mpesa', 'Mpesa'), ('card', 'Card')]) 
    payment_date = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    
    def __str__(self): return f"Payment of ${self.amount} for Booking {self.booking.room_number} by {self.user}"
