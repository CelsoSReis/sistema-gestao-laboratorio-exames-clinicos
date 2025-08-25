from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home', views.home, name='home'),

# CRUD Paciente
    path('pacientes/', views.PacienteListView.as_view(), name='paciente-list'),
    path('pacientes/novo/', views.PacienteCreateView.as_view(), name='paciente-create'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente-update'),
    path('pacientes/<int:pk>/excluir/', views.PacienteDeleteView.as_view(), name='paciente-delete'),

# URLs Dashboards
    path("dashboard/", views.redirect_dashboard, name="redirect_dashboard"),
    path("dashboard/admin/", views.dashboard_admin, name="dashboard_admin"),
    path("dashboard/recepcao/", views.dashboard_recepcao, name="dashboard_recepcao"),
    path("dashboard/biomedico/", views.dashboard_biomedico, name="dashboard_biomedico"),
    path("dashboard/tecnico/", views.dashboard_tecnico, name="dashboard_tecnico"),
    
# Rota redirecionamento
    path("redirect-dashboard/", views.redirect_dashboard, name="redirect_dashboard"),
]
