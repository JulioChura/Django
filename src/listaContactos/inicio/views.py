from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request):
    return HttpResponse("<h1>Hola desde mi app inicio</h1>")

def anotherView(request):
    return HttpResponse("<h1>Se ha creado la funcion anotherView</h1>")