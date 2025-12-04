from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from usuarios.decorators import group_required


# ---------------------------
# LOGIN / LOGOUT
# ---------------------------

class CustomLoginView(LoginView):
    template_name = "usuarios/login.html"


class CustomLogoutView(LogoutView):
    next_page = "/login/"


# ---------------------------
# VIEWS POR GRUPO
# ---------------------------

@group_required("Recepção")
def cadastro_paciente(request):
    return render(request, "index.html")


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


# ---------------------------
# REDIRECIONAMENTO PÓS-LOGIN
# ---------------------------

def redirecionar_pos_login(request):
    user = request.user

    if user.groups.filter(name="Recepção").exists():
        return redirect("index")

    if user.groups.filter(name="Médico").exists():
        return redirect("criar_pedido")

    if user.groups.filter(name="Técnico").exists():
        return redirect("registrar_exame")

    if user.groups.filter(name="Financeiro").exists():
        return redirect("financeiro_dashboard")

    if user.groups.filter(name="Paciente").exists():
        return redirect("visualizar_resultados")

    # Superusuário ou usuários sem grupo
    return redirect("index")


# ---------------------------
# VIEW PRINCIPAL (INDEX)
# ---------------------------

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")
