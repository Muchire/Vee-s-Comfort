from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'check_in', 'check_out', 'include_breakfast', 'include_lunch', 'airport_pickup_option', 'flight_number', 'pickup_time', 'car_type', 'room_service']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'pickup_time': forms.TimeInput(attrs={'type': 'time'}),
        }
