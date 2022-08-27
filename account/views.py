from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.


class SignInView(LoginView):
    template_name = 'account/login.html'
