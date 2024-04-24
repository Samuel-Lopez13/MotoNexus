from django.urls import path

from .views import home, ingresar, exit

urlpatterns = [
    path('', home, name='home'),
    path('ingresar/', ingresar, name='ingresar'),
    path('logout/', exit, name='exit'),
]