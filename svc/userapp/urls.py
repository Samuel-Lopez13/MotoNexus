from django.urls import path

from .views import buscador, productoInfo, carritoCompras, agregarCarrito, eliminarCarrito

urlpatterns = [
    path('buscardor/', buscador, name='buscador'),
    path('carrito/', carritoCompras, name='carritoCompras'),
    path('info_producto/<int:id>', productoInfo, name='productoInfo'),

    #path('agregar_carrito/<int:id>', MostrarCarrito),
    path('agregar_carrito/<int:id>', agregarCarrito),
    path('eliminar_carrito/<int:id>', eliminarCarrito),
]