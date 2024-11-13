from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Hostel


def home(request):
    return render(request, 'registration/home.html')

def login(request):
    return render(request, 'registration/login.html')

def index(request):
    return render(request, 'index.html')

def basepage(request):
    return render(request, 'hostel_pages/basepage.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def hostel_list(request):
    hostels=Hostel.objects.all()
    return render(request,'hostel_pages/hostel_list.html',{'hostels':hostels})

def hostel_detail(request, pk): 
    hostel = get_object_or_404(Hostel, pk=pk) 
    return render(request, 'hostel_pages/hostel_detail.html', {'hostel': hostel})