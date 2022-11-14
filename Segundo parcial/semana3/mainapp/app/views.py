from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenida(request):
    personas = Persona.objects.order_by('id')
    return render(request, 'index.html', {'personas': personas})