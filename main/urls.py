from django.urls import path
from .views import *

urlpatterns = [
    path("", mp_view, name='mainpage')
]