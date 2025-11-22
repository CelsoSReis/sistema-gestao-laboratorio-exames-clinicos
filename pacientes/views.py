from django.shortcuts import render, redirect
from .models import Paciente

def cadastrar_paciente(request):
    return render(request, "recepcao/cad_pacientes.html")

def salvar_paciente(request):
    if request.method == "POST":
        Paciente.objects.create(
            nome=request.POST.get("nome"),
            nome_social=request.POST.get("nome_social"),
            codigo=request.POST.get("codigo"),
            nascimento=request.POST.get("nascimento"),
            celular=request.POST.get("celular"),
            telefone=request.POST.get("telefone"),
            email=request.POST.get("email"),
            cep=request.POST.get("cep"),
            estado=request.POST.get("estado"),
            municipio=request.POST.get("municipio"),
            logradouro=request.POST.get("logradouro"),
        )

        return redirect("lista_pacientes")

    return redirect("cadastrar_paciente")

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/lista.html", {"pacientes": pacientes})

