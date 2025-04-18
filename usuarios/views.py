from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def dashboard_medico(request):
    if request.user.perfil.tipo != 'medico':
        return render(request, 'usuarios/sem_permissao.html')
    return render(request, 'usuarios/dashboard_medico.html')

@login_required
def dashboard_recepcionista(request):
    if request.user.perfil.tipo != 'recepcionista':
        return render(request, 'usuarios/sem_permissao.html')
    return render(request, 'recepcao/dashboard_recepcionista.html')

@login_required
def painel_admin(request):
    if request.user.perfil.tipo != 'admin':
        return render(request, 'usuarios/sem_permissao.html')
    return render(request, 'usuarios/painel_admin.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)

            tipo = user.perfil.tipo
            if tipo == 'medico':
                return redirect('dashboard_medico')
            elif tipo == 'recepcionista':
                return redirect('dashboard_recepcionista')
            elif tipo == 'admin':
                return redirect('painel_admin')
            else:
                return redirect('/')  # ou outra view padrão
        else:
            return render(request, 'usuarios/login.html', {'erro': 'Usuário ou senha inválidos'})

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
