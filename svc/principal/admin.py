from django.contrib import admin

from .models import Proveedores, Marcas, Productos

admin.site.register(Proveedores)
admin.site.register(Marcas)
admin.site.register(Productos)