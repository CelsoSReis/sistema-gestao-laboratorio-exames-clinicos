from rest_framework import permissions

class PermissaoPorPapel(permissions.BasePermission):
    """
    Permissão baseada no papel do usuário.
    """

    def has_permission(self, request, view):
        # Usuários admins sempre podem tudo
        if request.user.is_authenticated and request.user.papel == "admin":
            return True

        # Mapear papéis e ações permitidas por view
        if view.basename == "paciente":
            # Recepção pode criar/editar pacientes
            if request.user.papel in ["recepcao"]:
                return True
            # Outros só podem ver
            return request.method in permissions.SAFE_METHODS

        if view.basename == "exame":
            # Técnico ou admin podem criar/editar exames
            return request.user.papel in ["tecnico"]

        if view.basename == "pedido":
            # Médico pode criar pedidos, recepção pode criar pedidos
            if request.user.papel in ["recepcao", "medico"]:
                return True
            # Outros só podem ver
            return request.method in permissions.SAFE_METHODS

        # Default: negar
        return False
