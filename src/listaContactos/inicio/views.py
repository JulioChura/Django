from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request):
    return HttpResponse("<h1>Hola desde mi app inicio</h1>")
