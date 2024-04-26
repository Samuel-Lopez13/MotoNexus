from django.shortcuts import render, redirect, get_object_or_404
from principal.models import Proveedores, Marcas, Productos


def proveedores(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        img = request.FILES.get('img')

        # Crear una instancia del modelo Proveedores con los datos del formulario
        proveedor = Proveedores(nombre=nombre, img=img, stock=0, noVenta=0, status='Activo')

        # Guardar el proveedor en la base de datos
        proveedor.save()

        # Redirigir a una página de éxito o a donde desees
        return redirect(request.path)

    proveedores = Proveedores.objects.all()

    return render(request, 'inventario-proveedores.html', {'proveedores': proveedores})

def eliminarProveedor(request, id):
    proveedor = get_object_or_404(Proveedores, pk=id)
    if proveedor:
        proveedor.delete()

    return redirect('proveedores')

def marcas(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        img = request.FILES.get('img')
        proveedor_seleccionado = request.POST.get('opciones')

        # Crear una instancia del modelo Proveedores con los datos del formulario
        marca = Marcas(nombre=nombre, img=img, stock=0, noVenta=0, proveedor_id=proveedor_seleccionado, status='Activo')

        # Guardar el proveedor en la base de datos
        marca.save()

        # Redirigir a una página de éxito o a donde desees
        return redirect(request.path)

    marcas = Marcas.objects.all()
    proveedores = Proveedores.objects.all()

    return render(request, 'inventario-marcas.html', {'marcas': marcas, 'proveedores': proveedores})

def eliminarMarca(request, id):
    marca = get_object_or_404(Marcas, pk=id)
    if marca:
        marca.delete()

    return redirect('marcas')

def productos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        img = request.FILES.get('img')
        proveedor_seleccionado = request.POST.get('opciones-proveedor')
        marca_seleccionado = request.POST.get('opciones-marca')
        stock = request.POST.get('stock')

        # Crear una instancia del modelo Proveedores con los datos del formulario
        productos = Productos(nombre=nombre, descripcion=descripcion, precio=precio, img=img, stock=stock, noVenta=0, marca_id=marca_seleccionado, proveedor_id=proveedor_seleccionado, status='Activo')

        # Guardar el proveedor en la base de datos
        productos.save()

        # Redirigir a una página de éxito o a donde desees
        return redirect(request.path)

    productos = Productos.objects.all()
    proveedores = Proveedores.objects.all()
    marcas = Marcas.objects.all()

    return render(request, 'inventario-productos.html',{'productos': productos, 'proveedores': proveedores, 'marcas': marcas})