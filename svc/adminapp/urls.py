from django.urls import path

from .views import proveedores, marcas, productos, eliminarProveedor

urlpatterns = [
    path('proveedores/', proveedores, name='proveedores'),
    path('marcas/', marcas, name='marcas'),
    path('productos/', productos, name='productos'),

    path('eliminar_proveedor/<int:id>', eliminarProveedor)
]