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

    productos_en_carrito = Productos.objects.filter(id__in=carrito)

    total = sum(float(producto.precio) for producto in productos_en_carrito)

    # Pasar los productos al contexto de la plantilla
    context = {
        'carrito': productos_en_carrito,
        'total': total
    }

    return render(request, 'carrito.html', context)

def agregarCarrito(request, id):
    # Obtener el carrito actual de la sesión
    carrito = request.session.get('carrito', [])

    # Agregar el nuevo ID de producto al carrito
    carrito.append(id)

    # Actualizar el carrito en la sesión
    request.session['carrito'] = carrito

    #if id not in carrito:
        # Agregar el nuevo ID de producto al carrito
        #carrito.append(id)

        # Actualizar el carrito en la sesión
        #request.session['carrito'] = carrito

    return redirect('productoInfo', id=id)

def eliminarCarrito(request, id):
    carrito = request.session.get('carrito', [])

    try:
        carrito.remove(int(id))
        request.session['carrito'] = carrito
    except ValueError:
        pass  # Si el ID del producto no es válido, simplemente no hagas nada

    return redirect("carritoCompras")

#def MostrarCarrito(request, id):
    #carrito = request.session.get('carrito', [])
    #tamano_carrito = request.session.get('tamano_carrito', 0)

    # Imprimir el valor de tamano_carrito en la consola
    #print("El tamaño del carrito es:", tamano_carrito)

    #context = {
    #    'tamano_carrito': tamano_carrito
    #}

    #return render(request, 'home/index.html', context)