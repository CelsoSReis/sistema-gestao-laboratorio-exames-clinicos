from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from usuarios.decorators import group_required

class CustomLoginView(LoginView):
    template_name = "usuarios/login.html"

class CustomLogoutView(LogoutView):
    next_page = "/login/"

@group_required("Recepção")
def cadastro_paciente(request):
    return render(request, "recepcao/cadastro_paciente.html")

@group_required("Recepção")
def cad_paciente(request):
    return render(request, "recepcao/cad_pacientes.html")

@group_required("Médico")
def criar_pedido(request):
    return render(request, "criar_pedido.html")

@group_required("Técnico")
def registrar_exame(request):
    return render(request, "registrar_exame.html")

@group_required("Financeiro")
def financeiro_dashboard(request):
    return render(request, "financeiro_dashboard.html")

@group_required("Paciente")
def visualizar_resultados(request):
    return render(request, "visualizar_resultados.html")

from django.shortcuts import redirect

def redirecionar_pos_login(request):
    user = request.user

    if user.groups.filter(name="Recepção").exists():
        return redirect("cadastro_paciente")

    elif user.groups.filter(name="Médico").exists():
        return redirect("criar_pedido")

    elif user.groups.filter(name="Técnico").exists():
        return redirect("registrar_exame")

    elif user.groups.filter(name="Financeiro").exists():
        return redirect("financeiro_dashboard")

    elif user.groups.filter(name="Paciente").exists():
        return redirect("visualizar_resultados")

    # Superusuário ou sem grupo definido
    return redirect("index")