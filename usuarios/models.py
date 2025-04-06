from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    CARGOS = (
        ('admin', 'Administrador'),
        ('biomedico', 'Biomédico'),
        ('recepcionista', 'Recepcionista'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    cargo = models.CharField(max_length=20, choices=CARGOS)

    def __str__(self):
        return f"{self.user.username} ({self.get_cargo_display()})"
