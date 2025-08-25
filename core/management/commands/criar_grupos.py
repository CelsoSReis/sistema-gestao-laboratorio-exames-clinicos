from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Cria grupos de usuários e define permissões básicas"

    def handle(self, *args, **kwargs):
        # === Recepcionista ===
        recepcionista, _ = Group.objects.get_or_create(name="Recepcionista")
        perms_recepcao = [
            "add_paciente",
            "change_paciente",
            "view_paciente",
            "add_solicitacaoexame",
            "view_solicitacaoexame",
        ]
        self.add_permissions(recepcionista, perms_recepcao)

        # === Médico ===
        medico, _ = Group.objects.get_or_create(name="Médico")
        perms_medico = [
            "view_paciente",
            "view_solicitacaoexame",
            "change_solicitacaoexame",
        ]
        self.add_permissions(medico, perms_medico)

        # === Técnico de Laboratório ===
        tecnico, _ = Group.objects.get_or_create(name="Técnico")
        perms_tecnico = [
            "view_paciente",
            "view_exame",
            "view_solicitacaoexame",
            "change_solicitacaoexame",
        ]
        self.add_permissions(tecnico, perms_tecnico)

        # === Administrador ===
        administrador, _ = Group.objects.get_or_create(name="Administrador")
        administrador.permissions.set(Permission.objects.all())

        self.stdout.write(self.style.SUCCESS("✅ Grupos e permissões criados com sucesso!"))

    def add_permissions(self, group, codenames):
        for codename in codenames:
            try:
                perm = Permission.objects.get(codename=codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"⚠️ Permissão não encontrada: {codename}"))
