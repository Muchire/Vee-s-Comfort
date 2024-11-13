from django.urls import path,include
from .views import authView, basepage
from .views import home
from .views import index
from .views import login
from . import views


urlpatterns = [
    path("home/", home , name="home"),
    path("signup/", authView, name="authView"),
    path('login/', login, name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', index, name="index"),
    path('basepage/', basepage, name='basepage'),
]