from django.shortcuts import redirect, render, get_object_or_404
from personas.models import Persona
from personas.forms import PersonaForm
from django.contrib import messages

# Create your views here.
def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle_persona.html', {'persona': persona})

def crearPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            messages.info(request, 'Persona creada exitosamente.')
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'agregar_persona.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk = id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'editar_persona.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')
        