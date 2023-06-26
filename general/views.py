from django.shortcuts import render
from django.contrib import messages


# Create your views here.


def home_view(request):
    return render(request, 'general/home.html')


def about(request):
    return render(request, 'general/about.html')


def contact_us(request):
    user = request.user

    if request.method == "POST":

        messages.success(request, ('Thank you for your online enquiry, we will\
            contact you within the next 1-2 working days'))

        return render(request, 'general/home.html')

    return render(request, 'general/contact_us.html', {'user': user})
