from django.shortcuts import render
from principal.models import Productos


def buscador(request):
    if request.method == 'POST':
        # Obtener el texto de búsqueda del formulario
        texto_busqueda = request.POST.get('buscador__productos')

        productos = Productos.objects.filter(nombre__icontains=texto_busqueda)

        # Pasar el texto de búsqueda como contexto a la plantilla informacion
        return render(request, 'Busqueda.html', {'productos': productos})