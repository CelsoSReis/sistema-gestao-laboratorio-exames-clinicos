from django.shortcuts import redirect

def tipo_usuario_requerido(tipo_esperado):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.perfil.tipo != tipo_esperado:
                return redirect('login')  # ou uma página de acesso negado
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
