from django.contrib.auth.models import Group

def user_belongs_to_admin_group(user):
    # Verificar si el usuario pertenece al grupo de administradores
    admin_group = Group.objects.get(name='Admin')
    return user.groups.filter(name=admin_group).exists()