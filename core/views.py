from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Paciente
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden

# Home protegida
@login_required(login_url='/login')
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


## Redirecionamentos de perfis
# === Funções ===

@login_required
def redirect_dashboard(request):
    role = request.user.role

    if role == "admin":
        return redirect("dashboard_admin")
    elif role == "recepcao":
        return redirect("dashboard_recepcao")
    elif role == "biomedico":
        return redirect("dashboard_biomedico")
    elif role == "tecnico":
        return redirect("dashboard_tecnico")
    else:
        return redirect("admin:index")  # fallback
        

@login_required
def dashboard_admin(request):
    if request.user.role != "admin":
        return HttpResponseForbidden("Acesso negado.")
    return render(request, "dashboards/admin.html")


@login_required
def dashboard_recepcao(request):
    if request.user.role != "recepcao":
        return HttpResponseForbidden("Acesso negado.")
    return render(request, "dashboards/recepcao.html")


@login_required
def dashboard_biomedico(request):
    if request.user.role != "biomedico":
        return HttpResponseForbidden("Acesso negado.")
    return render(request, "dashboards/biomedico.html")


@login_required
def dashboard_tecnico(request):
    if request.user.role != "tecnico":
        return HttpResponseForbidden("Acesso negado.")
    return render(request, "dashboards/tecnico.html")
