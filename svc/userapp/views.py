from django.shortcuts import render, get_object_or_404
from principal.models import Productos, Marcas


def buscador(request):
    if request.method == 'POST':
        # Obtener el texto de búsqueda del formulario
        texto_busqueda = request.POST.get('buscador__productos')

        productos = Productos.objects.filter(nombre__icontains=texto_busqueda)
        cantidad = len(productos)

        marcas = Marcas.objects.values('nombre').distinct()

        # Pasar el texto de búsqueda como contexto a la plantilla informacion
        return render(request, 'Busqueda.html', {'productos': productos, 'cantidad': cantidad, 'texto_busqueda': texto_busqueda, 'marcas': marcas})

def productoInfo(request, id):
    producto = get_object_or_404(Productos, pk=id)
    return render(request, 'producto-selected.html', {"producto": producto})