from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def controle_pacientes(request):
    # Renderiza página dashboard
    return render(request, 'pacientes.html')