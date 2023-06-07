from django.shortcuts import render
from django.http import HttpResponse
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

def module_1(request):
    return render(request, 'pages/_html/module_1.html')

def modules(request):
    return render(request, 'pages/_html/modules.html')

def rec_pass(request):
    return render(request, 'pages/_html/rec_pass.html')
