from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request):
    varriables = {
        "name":"Julio"
    }
    return render(request, "home.html", varriables)

def anotherView(request):
    return HttpResponse("<h1>Se ha creado la funcion anotherView</h1>")

def contacto(request): 
    return render(request, "contacto.html")