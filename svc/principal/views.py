from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .utils import user_belongs_to_admin_group

def home(request):
    belongs_to_admin_group = user_belongs_to_admin_group(request.user)

    if belongs_to_admin_group:
        return render(request, 'home-admin.html')
    else:
        return render(request, 'home.html')

def ingresar(request):
    return render(request, 'ingreso/login.html')

def exit(request):
    logout(request)
    return redirect('home')