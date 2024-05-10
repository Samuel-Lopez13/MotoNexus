from django.urls import path

from .views import home, ingresar, exit, register

urlpatterns = [
    path('', home, name='home'),
    path('ingresar/', ingresar, name='ingresar'),
    path('registro/', register, name='registro'),
    path('logout/', exit, name='exit'),
]