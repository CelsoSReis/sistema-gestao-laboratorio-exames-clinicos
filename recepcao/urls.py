# recepcao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_recepcao, name='dashboard_recepcao'),
]
