from django.db import models

# Models para cadastro de pascientes

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nome_mae = models.CharField(max_length=255, blank=True, null=True)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    cod_ibge = models.CharField(max_length=50, blank=True, null=True)
    tipo_logradouro = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero_rua = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=30, blank=True, null=True)
    cns = models.CharField(max_length=255, blank=True, null=True)
    passaporte = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome