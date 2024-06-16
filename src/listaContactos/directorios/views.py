from django.shortcuts import render
from .models import Directorio

def lista_directorios(request):
    directorios = Directorio.objects.all()
    return render(request, 'tu_app/lista_directorios.html', {'directorios': directorios})
