from django.shortcuts import render

# Create your views here.
def recepcao_atendimento(request):
    return render(request, "recepcao/dashboard_recepcionista.html")

#def iniciar_atendimento(request):
   # return render(request, "recepcao/atendimento.html")
