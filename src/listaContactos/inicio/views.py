from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request):
    return render(request, "home.html")
def anotherView(request):
    return HttpResponse("<h1>Se ha creado la funcion anotherView</h1>")