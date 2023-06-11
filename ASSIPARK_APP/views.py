from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehiculo
from .forms import VehiculoForm
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/_html/about.html')

def advantages(request):
    return render(request, 'pages/_html/advantages.html')

def contact(request):
    return render(request, 'pages/_html/contact.html')

def functions(request):
    return render(request, 'pages/_html/functions.html')

def login(request):
    return render(request, 'pages/_html/login.html')

def modules(request):
    return render(request, 'pages/_html/modules.html')

def rec_pass(request):
    return render(request, 'pages/_html/rec_pass.html')

def inicioApp(request):
    return render(request, 'pages/_html/inicioApp.html')

def registrarVehiculo(request):
    formulario=VehiculoForm(request.POST or None)  
    if formulario.is_valid():
        formulario.save()
        return redirect('inicioApp')        
    return render(request, 'pages/_html/registrarVehiculo.html', {'formulario':formulario})

def eliminarVehiculo(request, idPAramentro):
    vehiculo=Vehiculo.objects.get(id=idPAramentro)
    vehiculo.delete()
    return redirect('inicioAapp')