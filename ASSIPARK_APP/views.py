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
    inicioApp = Vehiculo.objects.all()
    return render(request, 'pages/_html/inicioApp.html', {'vehiculos' : inicioApp})

def description(request):
    description = Vehiculo.objects.all()
    return render(request, 'pages/_html/description.html', {'mas' : description})

def registrarVehiculo(request):
    formulario=VehiculoForm(request.POST or None)  
    if formulario.is_valid():
        formulario.save()
        return redirect('inicioApp')        
    return render(request, 'pages/_html/registrarVehiculo.html', {'formulario':formulario})

def editar(request, idParametro):
    vehiculo = Vehiculo.objects.get(id=idParametro)
    formulario=VehiculoForm(request.POST or None, request.FILES or None, instance=vehiculo)  
    if formulario.is_valid and request.method=='POST':
        formulario.save()
        return redirect('inicioApp')        
    return render(request, 'pages/_html/editar.html', {'formulario':formulario})

def eliminar(request, idParametro):
    vehiculo=Vehiculo.objects.get(id=idParametro)
    vehiculo.delete()
    return redirect('inicioApp')

def kevinGit(request):
    return redirect('https://github.com/Kcarrillor01')

def leninGit(request):
    return redirect('https://github.com/LeninAlexHer')

def davidGit(request):
    return redirect('https://github.com/DavidPulido2005')

def angelGit(request):
    return redirect('https://github.com/Yacreds')