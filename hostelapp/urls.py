from django.conf import settings
from django.urls import path,include
from .views import about, authView, basepage, book_hostel, booking_confirmation, hostel_detail, hostel_list, login, login_view, logout_view,  payment, payment_confirmation
from .views import home
from .views import index
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path("home/", home , name="home"),
    path("signup/", authView, name="authView"),
    path('about/', about, name='about'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', index, name="index"),
    path('basepage/', basepage, name='basepage'),
    path('hostels/',hostel_list,name='hostel_list'),
    path('hostel/<int:pk>/', hostel_detail, name='hostel_detail'),
    path('hostels/<int:pk>/book/', book_hostel, name='book_hostel'),
    path('booking/confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('payment/<int:booking_id>/', payment, name='payment'),
    path('payment/confirmation/<int:payment_id>/', payment_confirmation, name='payment_confirmation'),
    path('booking_confirmation_pdf/<int:booking_id>/', views.booking_confirmation_pdf, name='booking_confirmation_pdf'),
    path('logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)