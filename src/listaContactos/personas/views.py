from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView

from .models import Persona
from .forms import PersonaForm, RawPersonaForm

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
    queryset = Persona.objects.filter(edad__lte='40')

def personaAnotherCreateView(request):
    form = RawPersonaForm()
    context = {
        'form':  form,
    }
    return render(request, 'personas/personasCreate.html', context)

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador'
    ]
    # Specify the correct template
