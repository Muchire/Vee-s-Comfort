from django.contrib import admin
from .models import Hostel, HostelImage, Booking, Meal

class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night')

class HostelImageAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'image')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'user', 'room_number', 'check_in', 'check_out', 'total_price')

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostel', 'price')

admin.site.register(Hostel, HostelAdmin)
admin.site.register(HostelImage, HostelImageAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Meal, MealAdmin)
