from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from hostelapp.forms import BookingForm

from .models import Booking, Hostel


def home(request):
    return render(request, 'registration/home.html')

def login(request):
    return render(request, 'registration/login.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def basepage(request):
    return render(request, 'hostel_pages/basepage.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/login.html')  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def hostel_list(request):
    hostels=Hostel.objects.all()
    return render(request,'hostel_pages/hostel_list.html',{'hostels':hostels})

def hostel_detail(request, pk): 
    hostel = get_object_or_404(Hostel, pk=pk) 
    return render(request, 'hostel_pages/hostel_detail.html', {'hostel': hostel})

@login_required 
def booking_confirmation(request, booking_id): 
    booking = get_object_or_404(Booking, pk=booking_id) 
    return render(request, 'hostel_pages/booking_confirmation.html', {'booking':booking})

def book_hostel(request, pk): 
    hostel = get_object_or_404(Hostel, pk=pk) 
    if request.method == 'POST': 
        form = BookingForm(request.POST) 
        if form.is_valid(): booking = form.save(commit=False) 
        booking.user = request.user 
        booking.hostel = hostel 
        nights = (booking.check_out - booking.check_in).days 
        booking.total_price = nights * hostel.price_per_night 
        booking.save() 
        return redirect('hostelapp:booking_confirmation', booking_id=booking.id) 
    else: form = BookingForm() 
    return render(request, 'hostel_pages/book_hostel.html', {'form':form, 'hostel':hostel})

