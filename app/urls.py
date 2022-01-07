from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('dash/',dashboard,name='dashboard'),
    path('hostel/',hostel,name='hostel'),
]