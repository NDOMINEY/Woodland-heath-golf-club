from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'general/home.html')


def contact_us(request):
    return render(request, 'general/contact_us.html')
