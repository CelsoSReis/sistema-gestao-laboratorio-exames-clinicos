from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "papel", "is_staff", "is_superuser")
    list_filter = ("papel", "is_staff", "is_superuser")
    search_fields = ("username", "email")
