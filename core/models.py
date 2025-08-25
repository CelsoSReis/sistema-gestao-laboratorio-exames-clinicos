from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('biomedico', 'Biomédico'),
        ('recepcao', 'Recepcionista'),
        ('tecnico', 'Técnico'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Exame(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('coletado', 'Coletado'),
            ('concluido', 'Concluído'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendente'
    )

    def __str__(self):
        return f"{self.paciente.nome} - {self.exame.nome} em {self.data_hora}"

class Laudo(models.Model):
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    resultado = models.TextField()
    data_emissao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='laudos/', blank=True, null=True)

    def __str__(self):
        return f"Laudo de {self.agendamento.paciente.nome} - {self.agendamento.exame.nome}"
