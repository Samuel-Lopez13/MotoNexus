from django.contrib.auth.models import Group

def user_belongs_to_admin_group(user):
    # Verificar si el usuario pertenece al grupo de administradores
    admin_group = Group.objects.get(name='Admin')
    return user.groups.filter(name=admin_group).exists()

def tamano_carrito(request):
    carrito = request.session.get('carrito', [])
    # Obtener el tamaño del carrito contando la cantidad de elementos
    tamano_carrito = len(carrito)
    # Pasar los productos al contexto de la plantilla
    context = {
        'tamano_carrito': tamano_carrito
    }
    return context

#pip install mysqlclient -- installar mysql
#pip install cloudinary -- instalar cloudinary
#pip install cloudinary-storage