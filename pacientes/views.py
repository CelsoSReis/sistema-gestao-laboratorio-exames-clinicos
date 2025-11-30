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
            nome_mae=request.POST.get("nome_mae"),
            nome_pai=request.POST.get("nome_pai"),
            nascimento=request.POST.get("nascimento"),
            sexo=request.POST.get("sexo"),
            celular=request.POST.get("celular"),
            telefone=request.POST.get("telefone"),
            email=request.POST.get("email"),
            cep=request.POST.get("cep"),
            estado=request.POST.get("estado"),
            municipio=request.POST.get("municipio"),
            cod_ibge=request.POST.get("cod_ibge"),
            tipo_logradouro=request.POST.get("tipo_logradouro"),
            logradouro=request.POST.get("logradouro"),
            numero_rua=request.POST.get("numero_rua"),
            bairro=request.POST.get("bairro"),
            complemento=request.POST.get("complemento"),
            cpf=request.POST.get("cpf"),
            rg=request.POST.get("rg"),
            cns=request.POST.get("cns"),
            passaporte=request.POST.get("passaporte"),
            observacoes=request.POST.get("observacoes"),
        )

        return redirect("lista_pacientes")

    return redirect("lista_pacientes")

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "recepcao/atendimento.html", {"pacientes": pacientes})

