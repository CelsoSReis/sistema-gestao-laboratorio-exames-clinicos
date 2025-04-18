from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('medico/', views.dashboard_medico, name='dashboard_medico'),
    path('recepcao/', views.dashboard_recepcionista, name='dashboard_recepcionista'),
    path('admin-panel/', views.painel_admin, name='painel_admin'),
]
