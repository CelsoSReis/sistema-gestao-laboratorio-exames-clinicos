from rest_framework import viewsets
from .models import Paciente, Exame, Pedido
from .serializers import PacienteSerializer, ExameSerializer, PedidoSerializer
from .permissoes import PermissaoPorPapel
from django.shortcuts import render, redirect


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [PermissaoPorPapel]

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    permission_classes = [PermissaoPorPapel]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [PermissaoPorPapel]

# Cadastrar Paciente

def cad_paciente(request):

    if request.method == "POST":
        data_nascimento = request.POST.get("nasc")

        # Garante que a data está no formato certo antes de salvar
        if data_nascimento:
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            except ValueError:
                data_nascimento = None
        else:
            data_nascimento = None

    if request.method == "POST":
        Paciente.objects.create(
            nome_completo=request.POST.get("nome_completo"),
            endereco=request.POST.get("endereco"),
            complemento=request.POST.get("complemento"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
            cep=request.POST.get("cep"),
            telefone=request.POST.get("telefone"),
            celular=request.POST.get("celular"),
            email=request.POST.get("email"),
            rg=request.POST.get("rg"),
            orgao_exp=request.POST.get("orgao_exp"),
            cpf=request.POST.get("cpf"),
            data_nascimento=request.POST.get("data_nascimento"),
            cor=request.POST.get("cor"),
            nome_mae=request.POST.get("nome_mae"),
            nome_pai=request.POST.get("nome_pai"),
            estado_civil=request.POST.get("estado_civil"),
            escolaridade=request.POST.get("escolaridade"),
            plano_convenio=request.POST.get("plano_convenio"),
            profissao=request.POST.get("profissao"),
            observacoes=request.POST.get("observacoes"),
        )
        return redirect("cadastro_paciente")  # depois pode mudar para "lista_pacientes" ou outra view
    
    return render(request, "recepcao/cad_pacientes.html")

# Exibir pacientes cadastrados

def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by("-id")  # lista do mais novo para o mais antigo
    return render(request, "recepcao/cadastro_paciente.html", {"pacientes": pacientes})
