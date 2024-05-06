from django.shortcuts import render, get_object_or_404, redirect
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

def carritoCompras(request):
    carrito = request.session.get('carrito', [])

    # Pasar el contenido del carrito al contexto de la plantilla
    #context = {
    #    'carrito': carrito
    #}

    productos_en_carrito = Productos.objects.filter(id__in=carrito)

    # Pasar los productos al contexto de la plantilla
    context = {
        'carrito': productos_en_carrito
    }

    return render(request, 'carrito.html', context)

def agregarCarrito(request, id):
    # Obtener el carrito actual de la sesión
    carrito = request.session.get('carrito', [])

    if id not in carrito:
        # Agregar el nuevo ID de producto al carrito
        carrito.append(id)

        # Actualizar el carrito en la sesión
        request.session['carrito'] = carrito

    return redirect('productoInfo', id=id)