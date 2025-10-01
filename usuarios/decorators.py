from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def group_required(group_name):
    """Restringe o acesso a usuários de um grupo específico"""
    def in_group(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_group)
