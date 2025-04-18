from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    TIPOS = [
        ('admin', 'Administrador'),
        ('medico', 'Médico'),
        ('recepcionista', 'Recepcionista'),
        ('paciente', 'Paciente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ({self.tipo})'


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance, tipo='paciente')  # tipo padrão

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()
