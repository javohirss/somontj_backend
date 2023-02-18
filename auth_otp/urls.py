from django.urls import path
from .views import *

urlpatterns = [
    path('otp/', OTPView, name='otp_login'),
]