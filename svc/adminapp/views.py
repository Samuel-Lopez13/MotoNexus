from django.shortcuts import render, redirect, get_object_or_404
from principal.models import Proveedores, Marcas

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

        # Crear una instancia del modelo Proveedores con los datos del formulario
        marca = Marcas(nombre=nombre, img=img, stock=0, noVenta=0, proveedor_id=1, status='Activo')

        # Guardar el proveedor en la base de datos
        marca.save()

        # Redirigir a una página de éxito o a donde desees
        return redirect(request.path)

    marcas = Marcas.objects.all()

    return render(request, 'inventario-marcas.html', {'marcas': marcas})

def productos(request):
    return render(request, 'inventario-productos.html')