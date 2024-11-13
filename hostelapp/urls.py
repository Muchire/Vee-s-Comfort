from django.conf import settings
from django.urls import path,include
from .views import authView, basepage, hostel_detail, hostel_list
from .views import home
from .views import index
from .views import login
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("home/", home , name="home"),
    path("signup/", authView, name="authView"),
    path('login/', login, name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', index, name="index"),
    path('basepage/', basepage, name='basepage'),
    path('hostels/',hostel_list,name='hostel_list'),
    path('hostel/<int:pk>/', hostel_detail, name='hostel_detail'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)