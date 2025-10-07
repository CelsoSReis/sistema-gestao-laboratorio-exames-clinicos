from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    # Rotas da API

    # Rota para o formulário de cadastro
    path("atendimento/", views.iniciar_atendimento, name="iniciar_atendimento"),
]
