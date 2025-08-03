from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home', views.home, name='home'),

# CRUD Paciente
    path('pacientes/', views.PacienteListView.as_view(), name='paciente-list'),
    path('pacientes/novo/', views.PacienteCreateView.as_view(), name='paciente-create'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente-update'),
    path('pacientes/<int:pk>/excluir/', views.PacienteDeleteView.as_view(), name='paciente-delete'),
]
