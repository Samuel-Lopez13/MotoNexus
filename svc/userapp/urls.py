from django.urls import path

from .views import buscador

urlpatterns = [
    path('buscardor/', buscador, name='buscador'),
]