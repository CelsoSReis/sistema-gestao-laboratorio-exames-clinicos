from django.db import models
from django.conf import settings
import uuid

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo

class Exame(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ("agendado", "Agendado"),
        ("coletado", "Coletado"),
        ("em_analise", "Em análise"),
        ("finalizado", "Finalizado"),
        ("cancelado", "Cancelado"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    solicitado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    exames = models.ManyToManyField(Exame)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="agendado")
    protocolo = models.CharField(max_length=100, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.protocolo} - {self.paciente.nome_completo}"
