from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

# Permissões REAIS de acordo com seus apps atuais
GRUPOS = {
    "Administrador": [],

    "Recepção": [
        ("pacientes", "add_paciente"),
        ("pacientes", "view_paciente"),
        ("pacientes", "change_paciente"),
    ],

    "Médico": [
        # Nenhum model existe ainda neste app — deixamos vazio por enquanto
    ],

    "Técnico": [
        # No momento não existe o app laboratorio — vazio
    ],

    "Financeiro": [
        # O app financeiro ainda não existe — vazio
    ],

    "Paciente": [
        ("pacientes", "view_paciente"),
    ],
}


class Command(BaseCommand):
    help = "Cria grupos e atribui permissões disponíveis no projeto"

    def handle(self, *args, **kwargs):
        for nome_grupo, permissoes in GRUPOS.items():
            grupo, _ = Group.objects.get_or_create(name=nome_grupo)

            for app_label, codename in permissoes:
                try:
                    perm = Permission.objects.get(
                        codename=codename,
                        content_type__app_label=app_label
                    )
                    grupo.permissions.add(perm)
                except Permission.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Permissão não encontrada: {app_label}.{codename}"
                        )
                    )

            grupo.save()
            self.stdout.write(
                self.style.SUCCESS(f"Grupo '{nome_grupo}' configurado!")
            )
