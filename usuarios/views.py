from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = "usuarios/login.html"

class CustomLogoutView(LogoutView):
    next_page = "/login/"
