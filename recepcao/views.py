# recepcao/views.py
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login')
def dashboard_recepcao(request):
    if not hasattr(request.user, 'perfil') or request.user.perfil.cargo != 'recepcionista':
        return HttpResponseForbidden("Acesso negado")
    return render(request, 'dashboard.html')
