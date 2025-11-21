from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    # Rotas da API

    # Rota para o formulário atendimento
    path("atendimento/", views.iniciar_atendimento, name="iniciar_atendimento"),
    path("recepcao/", views.recepcao_atendimento, name="recepcao_atendimento"),
]
