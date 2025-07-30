from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Paciente

# Home protegida
def home(request):
    return render(request, 'core/home.html')

# Login / Logout
class LoginUsuario(LoginView):
    template_name = 'core/login.html'

class LogoutUsuario(LogoutView):
    next_page = 'login'

# Lista
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/pacientes/list.html'
    context_object_name = 'pacientes'

# Criar
class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'data_nascimento', 'cpf', 'telefone', 'email']
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('paciente-list')

# Atualizar
class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nome', 'data_nascimento', 'cpf', 'telefone', 'email']
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('paciente-list')

# Excluir
class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'core/pacientes/confirm_delete.html'
    success_url = reverse_lazy('paciente-list')
