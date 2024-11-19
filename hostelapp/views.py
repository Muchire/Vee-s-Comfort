from smtplib import SMTPAuthenticationError
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import BadHeaderError, HttpResponse
from django.urls import reverse
from weasyprint import HTML
from django.core.mail import send_mail 
from django.template.loader import render_to_string
# from hostelapp.forms import BookingForm
from django.contrib.auth import logout
from .models import Booking, Hostel, Payment
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Booking, AirportPickup, Meal, Hostel
# from .forms import BookingForm, AirportPickupForm

def home(request):
    return render(request, 'registration/home.html')


def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def basepage(request):
    return render(request, 'hostel_pages/basepage.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('hostelapp:index')  # Ensure this redirects to the correct URL name



def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostelapp:hostel_list')  # Redirect to the index page or another page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form": form})

def hostel_list(request):
    hostels=Hostel.objects.all()
    return render(request,'hostel_pages/hostel_list.html',{'hostels':hostels})


def hostel_detail(request, pk): 
    hostel = get_object_or_404(Hostel, pk=pk) 
    print(hostel.images.all())
    return render(request, 'hostel_pages/hostel_detail.html', {'hostel': hostel})


def booking_confirmation(request, booking_id): 
    booking = get_object_or_404(Booking, pk=booking_id) 
    return render(request, 'hostel_pages/booking_confirmation.html', {'booking':booking})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm

@login_required
def book_hostel(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.hostel = hostel
            booking.save()
            return redirect('hostelapp:booking_confirmation', booking_id=booking.id)  # Redirect to a success page
    else:
        form = BookingForm()
    
    return render(request,  'hostel_pages/book_hostel.html', {'form': form, 'hostel': hostel})

# def book_hostel(request, pk):
#     hostel = get_object_or_404(Hostel, pk=pk)
#     if request.method == 'POST':
#         form = UnifiedBookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.hostel = hostel
#             nights = (booking.check_out - booking.check_in).days
#             booking.total_price = nights * hostel.price_per_night

#             # Calculate total price for extra services
#             if form.cleaned_data['room_service']:
#                 booking.room_service = True
#                 booking.total_price += 1000

#             if form.cleaned_data['airport_pickup']:
#                 booking.airport_pickup = True
#                 booking.total_price += 500
#                 AirportPickup.objects.create(
#                     booking=booking,
#                     user=request.user,
#                     pickup_time=form.cleaned_data['pickup_time'],
#                     flight_number=form.cleaned_data['flight_number'],
#                     vehicle_type=form.cleaned_data['vehicle_type'],
#                     price=500
#                 )

#             if form.cleaned_data['tour_guide']:
#                 booking.tour_guide = True
#                 booking.total_price += 800
#                 TourGuideService.objects.create(
#                     booking=booking,
#                     user=request.user,
#                     guide_name=form.cleaned_data['guide_name'],
#                     price=800,
#                     tour_date=form.cleaned_data['tour_date']
#                 )

#             booking.save()

#             # Save selected meals and add their prices to the total price
#             selected_meals = form.cleaned_data['meals']
#             booking.meals.set(selected_meals)
#             for meal in selected_meals:
#                 MealService.objects.create(booking=booking, user=request.user, meal_type=meal.name, price=meal.price, served_date=booking.check_in)
#                 booking.total_price += meal.price

#             booking.save()  # Save the updated total price

#             # Send Confirmation Email (ensure you have the function defined)
#             # send_booking_confirmation_email(request.user, booking)

#             return redirect('hostelapp:booking_confirmation', booking_id=booking.id)
#     else:
#         form = UnifiedBookingForm()
#     return render(request, 'hostel_pages/book_hostel.html', {'form': form, 'hostel': hostel})


def payment_confirmation(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payment/payment_confirmation.html', {'payment': payment})

def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        phone_number = request.POST.get('phone_number', None)  # Only for Mpesa

        # Create a payment record
        payment = Payment(
            booking=booking,
            user=request.user,
            amount=booking.total_price,
            payment_method=payment_method,
            status='pending'
        )
        payment.save()
        
        # Handle the payment logic here (e.g., initiate Mpesa transaction)
        if payment_method == 'mpesa':
            # initiate_mpesa_transaction(payment.amount, phone_number)
            pass
        elif payment_method == 'card':
            return redirect('card_payment', payment_id=payment.id)

        return redirect('hostelapp:payment_confirmation', payment_id=payment.id)
    return render(request, 'payment/payment.html', {'booking': booking})
from django.shortcuts import render, get_object_or_404



def booking_confirmation_pdf(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    html_string = render(request, 'hostel_pages/booking_confirmation.html', {'booking': booking}).content.decode('utf-8')
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=booking_confirmation_{booking_id}.pdf'
    return response


def send_booking_confirmation_email(user, booking):
    subject = 'Booking Confirmation'
    message = render_to_string('hostel_pages/booking_confirmation_email.html', {
        'user': user,
        'booking': booking,
    })
    from_email = 'your_email@gmail.com'
    recipient_list = [user.email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except SMTPAuthenticationError as e:
        return HttpResponse(f'SMTP authentication error: {e}')
    except Exception as e:
        return HttpResponse(f'An error occurred: {e}')
