from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from laboratorio.views import PacienteViewSet, ExameViewSet, PedidoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"pacientes", PacienteViewSet)
router.register(r"exames", ExameViewSet)
router.register(r"pedidos", PedidoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include("usuarios.urls")),  # login/logout
    path("lab/", include("laboratorio.urls")),  # <-- aqui 'lab' é o nome do seu app
    path("at/", include("atendimento.urls")),  # <-- aqui 'at' é o nome do seu app
]