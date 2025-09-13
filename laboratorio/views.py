from rest_framework import viewsets
from .models import Paciente, Exame, Pedido
from .serializers import PacienteSerializer, ExameSerializer, PedidoSerializer
from .permissoes import PermissaoPorPapel

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [PermissaoPorPapel]

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    permission_classes = [PermissaoPorPapel]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [PermissaoPorPapel]
