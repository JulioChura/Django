from django.shortcuts import render, get_object_or_404
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
    
    print('GET :', request.GET )
    print('POST :', request.POST)
    context = {}
    return render(request, 'personas/personasCreate.html', context)
    #return render(request, 'personas/personasCreate.html', context)
    
    Esto manda los datos de la persona con id = 2 en los campos del formulario
    obj = Persona.objects.get(id=2)
    form = PersonaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form
    }
    """
    initialValues = {
        'nombres': "Sin nombre"
    }
    form = PersonaForm(request.POST  or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form
    }
    return render(request, 'personas/personasCreate.html', context)


def personasShowObject(request, myId):
    #obj = Persona.objects.get(id=myId)
    obj = get_object_or_404(Persona, id = myId)
    context  = {
        'object': obj,
    }
    return render(request, 'personas/description.html', context)


def searchForHelp(request):
    return render(request, 'personas/search.html', {})

class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='40')

def personaAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
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

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList': queryset
    }
    return render(request, 'personas/personasLista.html', context)