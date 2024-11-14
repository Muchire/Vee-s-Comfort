from django import forms
from .models import Booking
import random

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'check_out': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in'].input_formats = ['%Y-%m-%d']
        self.fields['check_out'].input_formats = ['%Y-%m-%d']

    def save(self, commit=True):
        booking = super().save(commit=False)
        booking.room_number = random.randint(1000, 9999)  # Generate a random 4-digit room number
        if commit:
            booking.save()
        return booking
