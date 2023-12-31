from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistration

# Create your views here.


def login_user(request):
    """ loads login user page and submits request to login if form completed """

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')

        else:
            messages.success(
                request, "There was an error logging in, please try again.")
            return redirect('login')

    else:
        return render(request, 'auth/login.html')


def logout_view(request):
    """ processes user logout and redirects to home page """

    logout(request)
    messages.success(
        request, "You have been logged out.")

    return render(request, 'general/home.html')


def register_user(request):
    """ loads registration  page and submits request to 
    register if form completed """

    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = UserRegistration()

    return render(request, 'auth/register.html', {'form': form})
