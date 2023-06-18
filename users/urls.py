from django.urls import path
from . views import login_user, logout_view

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', logout_view, name='logout'),
]
