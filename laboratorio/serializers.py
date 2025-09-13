from rest_framework import serializers
from .models import Paciente, Exame, Pedido

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = "__all__"

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
