from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from . import views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
