from django.contrib.auth.models import Group

def user_belongs_to_admin_group(user):
    # Verificar si el usuario pertenece al grupo de administradores
    admin_group = Group.objects.get(name='Admin')
    return user.groups.filter(name=admin_group).exists()

#pip install mysqlclient -- installar mysql
#pip install cloudinary -- instalar cloudinary
#pip install cloudinary-storage