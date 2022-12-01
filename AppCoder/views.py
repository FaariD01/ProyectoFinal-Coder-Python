from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from django.core import serializers
from AppCoder.forms import EquipoFormulario
from AppCoder.forms import EdificioFormulario
from AppCoder.forms import EncargadoFormulario


# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def edificios(request):

    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = EdificioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            edificio = Edificio(
                nombre_fantasia=informacion["nombre_fantasia"], direccion=informacion["direccion"], numero=informacion["numero"], mail_contacto=informacion['mail_contacto'])
            edificio.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EdificioFormulario()

    return render(request, "AppCoder/edificios.html", {"miFormulario": miFormulario})


def equipo(request):

    if request.method == "POST":

        # Aqui me llega la informacion del html
        miFormulario = EquipoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            equipo = Equipo(
                nombre=informacion["nombre"], apellido=informacion["apellido"], edad=informacion["edad"], num_contacto=informacion['num_contacto'], mail_contacto=informacion['mail_contacto'])
            equipo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EquipoFormulario()

    return render(request, "AppCoder/equipo.html", {"miFormulario": miFormulario})


def edificiosapi(request):
    edificios_todos = Edificio.objects.all()
    return HttpResponse(serializers.serialize('json', edificios_todos))


def equipoapi(request):
    equipo_todos = Equipo.objects.all()
    return HttpResponse(serializers.serialize('json', equipo_todos))


def encargadoapi(request):
    encargado_todos = Encargado.objects.all()
    return HttpResponse(serializers.serialize('json', encargado_todos))


def encargados(request):
    if request.method == "POST":

        # Aqui me llega la informacion del html
        miFormulario = EncargadoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            encargado = Encargado(
                nombre=informacion["nombre"], edad=informacion["edad"], num_contacto=informacion['num_contacto'], mail_contacto=informacion['mail_contacto'])
            encargado.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EncargadoFormulario()

    return render(request, "AppCoder/encargados.html", {"miFormulario": miFormulario})


def buscar(request):
    nombre_views = request.GET['nombre_fantasia']
    direccion_views = Edificio.objects.filter(nombre_fantasia=nombre_views)
    numero_views = Edificio.objects.filter(nombre_fantasia=nombre_views)
    return render(request, 'AppCoder/resultadoEdificio.html', {"nombre_fantasia": nombre_views, "direccion": direccion_views, "numero": numero_views})


def buscaredificio(request):
    return render(request, 'AppCoder/busquedaEdificio.html')
