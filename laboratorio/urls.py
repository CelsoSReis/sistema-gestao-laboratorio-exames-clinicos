from django.urls import path, include
from rest_framework import routers
from . import views
from .views import PacienteViewSet, ExameViewSet, PedidoViewSet, cad_paciente, listar_pacientes

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    # Rotas da API
    path('api/', include(router.urls)),

    # Rota para o formulário de cadastro
    path('cadastro-paciente/', cad_paciente, name='cad_paciente'),
    path("listar-pacientes/", views.listar_pacientes, name="cadastro_paciente"),
]
