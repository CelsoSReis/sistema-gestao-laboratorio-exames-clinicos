from django.urls import path
from . import views

urlpatterns = [
    path("pacientes/novo/", views.cadastrar_paciente, name="cadastrar_paciente"),
    path("pacientes/salvar/", views.salvar_paciente, name="salvar_paciente"),
    path("pacientes/", views.lista_pacientes, name="lista_pacientes"),
]
