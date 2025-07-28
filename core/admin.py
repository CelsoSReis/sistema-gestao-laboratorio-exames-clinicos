from django.contrib import admin
from .models import Usuario, Paciente, Exame, Agendamento, Laudo

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Exame)
admin.site.register(Agendamento)
admin.site.register(Laudo)
