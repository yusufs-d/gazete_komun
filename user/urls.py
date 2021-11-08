from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import path,include

app_name = "user"
Permission
from .views import *
urlpatterns = [
    path('register/',register,name="register"),
    path('login/',loginusr,name="login"),
    path('logout/',logoutusr,name="logout"),
]
