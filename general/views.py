from django.shortcuts import render 
from

# Create your views here.


def home_view(request):
    return render(request, 'general/home.html')


def contact_us(request):
    user = request.user

    return render(request, 'general/contact_us.html', {'user', user})
