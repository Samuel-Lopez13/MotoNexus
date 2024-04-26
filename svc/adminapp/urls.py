from django.urls import path

from .views import proveedores, marcas, productos, eliminarProveedor, eliminarMarca

urlpatterns = [
    path('proveedores/', proveedores, name='proveedores'),
    path('marcas/', marcas, name='marcas'),
    path('productos/', productos, name='productos'),

    path('eliminar_proveedor/<int:id>', eliminarProveedor),
    path('eliminar_marca/<int:id>', eliminarMarca)
]