# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib import messages
from django.contrib.messages import constants

#Função cadastro
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)

        if user is not None and hasattr(user, 'perfil'):
            login(request, user)
            cargo = user.perfil.cargo

            if cargo == 'administrador':
                return redirect('/admin/dashboard.html/')
            elif cargo == 'biomedico':
                return redirect('/biomedico/dashboard/')
            elif cargo == 'recepcionista':
                return redirect('dashboard_recepcao')
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorretos!')
    return render(request, 'bases/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


