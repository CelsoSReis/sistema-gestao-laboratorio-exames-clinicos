from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PAPEL_CHOICES = [
        ("admin", "Administrador"),
        ("recepcao", "Recepção"),
        ("tecnico", "Técnico de laboratório"),
        ("medico", "Médico"),
        ("paciente", "Paciente"),
        ("financeiro", "Financeiro"),
    ]
    papel = models.CharField(max_length=20, choices=PAPEL_CHOICES, default="paciente")
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_papel_display()})"
