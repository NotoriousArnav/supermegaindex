from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('/login', MyLoginView.as_view(), name='login'),
    path('/logout', auth_views.LogoutView.as_view(next_page="index"), name='logout'),
    path('/register', RegisterView.as_view(), name='register'),
]
