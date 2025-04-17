from django.db import models

# Create your models here.
"""class TipoExame(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    preparo = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

class Exame(models.Model):
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoExame, on_delete=models.CASCADE)
    data_coleta = models.DateTimeField()
    data_resultado = models.DateTimeField(blank=True, null=True)
    resultado = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('coletado', 'Coletado'), ('concluido', 'Concluído')])"""
