from django.shortcuts import render

# Create your views here.
def iniciar_atendimento(request):
    return render(request, "recepcao/atendimento.html")