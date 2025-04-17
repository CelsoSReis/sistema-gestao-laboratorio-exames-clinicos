from django.db import models
"""
# Create your models here.
class Pagamento(models.Model):
    exame = models.OneToOneField('exames.Exame', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_pagamento = models.DateField()
    metodo = models.CharField(max_length=20, choices=[('pix', 'Pix'), ('boleto', 'Boleto'), ('dinheiro', 'Dinheiro'), ('cartao', 'Cartão')])
"""