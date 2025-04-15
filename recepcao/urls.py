from django.urls import path
from . import views

urlpatterns = [
    path('convenios/', views.convenio_list, name='convenio_list'),
    path('convenios/novo/', views.convenio_create, name='convenio_create'),
    path('convenios/<int:pk>/editar/', views.convenio_update, name='convenio_update'),
    path('convenios/<int:pk>/excluir/', views.convenio_delete, name='convenio_delete'),
]