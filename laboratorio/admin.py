from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Exame, Pedido

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "cpf", "data_nascimento", "telefone", "email")
    search_fields = ("nome_completo", "cpf")

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "preco")
    search_fields = ("codigo", "nome")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("protocolo", "paciente", "solicitado_por", "status", "criado_em")
    search_fields = ("protocolo", "paciente__nome_completo", "solicitado_por__username")
