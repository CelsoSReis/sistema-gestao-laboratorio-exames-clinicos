from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("", index, name="index"),
]
