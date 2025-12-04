from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("redirecionar/", views.redirecionar_pos_login, name="redirecionar"),

    
    #path("cadastro-paciente/", views.cadastro_paciente, name="cadastro_paciente"),
    #path("criar-pedido/", views.criar_pedido, name="criar_pedido"),
    #path("registrar-exame/", views.registrar_exame, name="registrar_exame"),
    #path("financeiro-dashboard/", views.financeiro_dashboard, name="financeiro_dashboard"),
    #path("visualizar-resultados/", views.visualizar_resultados, name="visualizar_resultados"),
    
]
