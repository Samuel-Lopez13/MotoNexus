from django.urls import path

from .views import buscador, productoInfo

urlpatterns = [
    path('buscardor/', buscador, name='buscador'),
    path('info_producto/<int:id>', productoInfo)
]