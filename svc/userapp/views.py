from collections import Counter

from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from principal.models import Productos, Marcas

from principal.utils import tamano_carrito


def buscador(request):
    if request.method == 'POST':
        # Obtener el texto de búsqueda del formulario
        texto_busqueda = request.POST.get('buscador__productos')

        productos = Productos.objects.filter(nombre__icontains=texto_busqueda)
        cantidad = len(productos)

        marcas = Marcas.objects.values('nombre').distinct()

        context = tamano_carrito(request)

        # Pasar el texto de búsqueda como contexto a la plantilla informacion
        return render(request, 'Busqueda.html', {'productos': productos, 'cantidad': cantidad, 'texto_busqueda': texto_busqueda, 'marcas': marcas, **context})

def productoInfo(request, id):
    producto = get_object_or_404(Productos, pk=id)

    context = tamano_carrito(request)

    return render(request, 'producto-selected.html', {"producto": producto, **context})

def carritoCompras(request):
    carrito = request.session.get('carrito', [])

    # Contar la cantidad de veces que se repite cada ID en el carrito
    counter = Counter(carrito)

    productos_en_carrito = Productos.objects.filter(id__in=carrito)

    total = 0.0

    # Iterar sobre todos los IDs de productos en el carrito y sumar sus precios
    for producto_id in carrito:
        producto = Productos.objects.get(id=producto_id)
        total += float(producto.precio)

    # Obtener el tamaño del carrito contando la cantidad de elementos
    tamano_carrito = len(carrito)

    # Convertir el contador a un diccionario estándar
    contador_dict = dict(counter)

    # Pasar los productos al contexto de la plantilla
    context = {
        'carrito': productos_en_carrito,
        'total': total,
        'tamano_carrito': tamano_carrito,
        'contador_ids': contador_dict
    }

    return render(request, 'carrito.html', context)

def direccion(request):
    carrito = request.session.get('carrito', [])

    total = 0.0

    # Iterar sobre todos los IDs de productos en el carrito y sumar sus precios
    for producto_id in carrito:
        producto = Productos.objects.get(id=producto_id)
        total += float(producto.precio)

    # Obtener el tamaño del carrito contando la cantidad de elementos
    tamano_carrito = len(carrito)

    context = {
        'total': total,
        'tamano_carrito': tamano_carrito
    }

    return render(request, 'MetodoPago.html', context)

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

    # Obtener la URL actual
    redirect_url = request.META.get('HTTP_REFERER')

    return redirect(redirect_url, id=id)

def eliminarCarrito(request, id):
    carrito = request.session.get('carrito', [])

    try:
        carrito.remove(int(id))
        request.session['carrito'] = carrito
    except ValueError:
        pass  # Si el ID del producto no es válido, simplemente no hagas nada

    return redirect("carritoCompras")

def reducirStock(request):
    carrito = request.session.get('carrito', [])

    # Obtener un contador de los productos en el carrito
    counter = Counter(carrito)

    for producto_id, cantidad in counter.items():
        # Obtener el producto correspondiente de la base de datos
        producto = get_object_or_404(Productos, pk=producto_id)

        marca = producto.marca
        proveedor = producto.proveedor

        # Reducir el stock del producto según la cantidad en el carrito
        producto.stock -= cantidad
        producto.noVenta += cantidad
        producto.save()

        # Reducir el stock de la marca en función de la venta del producto
        marca.stock -= cantidad  # Puedes ajustar esto según tus necesidades
        marca.noVenta += cantidad
        marca.save()

        # Reducir el stock de la marca en función de la venta del producto
        proveedor.stock -= cantidad  # Puedes ajustar esto según tus necesidades
        proveedor.noVenta += cantidad
        proveedor.save()

    # Eliminar la clave 'carrito' de la sesión
    if 'carrito' in request.session:
        del request.session['carrito']

    return redirect("home")