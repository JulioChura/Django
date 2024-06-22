from django.shortcuts import render
from django.views.generic.list import  ( ListView, )

from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'nombre': obj.nombres,
        'edad': obj.edad
    }
    return render(request, 'personas/test.html', context)

def personaCreateView(request):
    """""
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form
    }
    """
    print('GET :', request.GET )
    print('POST :', request.POST)
    context = {}
    return render(request, 'personas/personasCreate.html', context)
    #return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

class PersonaListView(ListView):
    model = Persona