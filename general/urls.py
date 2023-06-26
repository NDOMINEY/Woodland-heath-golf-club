from django.contrib import admin
from django.urls import path
from . views import home_view, contact_us, about

urlpatterns = [
    path('', home_view, name='home'),
    path('contact', contact_us, name='contact_us'),
    path('about', about, name='about'),

]
