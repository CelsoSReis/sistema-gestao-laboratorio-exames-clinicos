from django.db import models
"""
# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    convenio = models.ForeignKey('Convenio', on_delete=models.SET_NULL, null=True, blank=True)
"""