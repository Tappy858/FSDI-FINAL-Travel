from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import SignupForm
from django.urls import reverse_lazy



# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'
    redirect_authenticated_user = True

    