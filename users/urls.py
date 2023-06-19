from django.urls import path
from . views import login_user, logout_view, register_user

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_user, name='register'),
]
