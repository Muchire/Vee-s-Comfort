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



class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hostel_images/')

class Booking(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10,blank=True, editable=False)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        if not self.room_number:
            self.room_number = str(random.randint(1000, 9999))
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.room_number} by {self.user}"
    
