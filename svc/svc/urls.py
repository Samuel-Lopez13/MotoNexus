from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

urlpatterns = [
    path('', include('principal.urls')),
    path('', include('adminapp.urls')),
    path('', include('userapp.urls')),
    path('admin/', admin.site.urls),

    #Es para obtener accedo a los sistemas de home, logout, change password
    path('accounts/', include('django.contrib.auth.urls')),
]