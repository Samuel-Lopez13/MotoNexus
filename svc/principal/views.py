from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate

from .forms import RegistrationForm
from .utils import user_belongs_to_admin_group, tamano_carrito


def home(request):
    belongs_to_admin_group = user_belongs_to_admin_group(request.user)

    context = tamano_carrito(request)

    if belongs_to_admin_group:
        return render(request, 'home-admin.html')
    else:
        return render(request, 'home.html', context)

def ingresar(request):
    return render(request, 'ingreso/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de registro exitoso
    else:
        form = RegistrationForm()
    return render(request, 'ingreso/registro.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('home')