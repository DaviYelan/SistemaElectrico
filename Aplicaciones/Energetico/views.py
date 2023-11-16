from django.shortcuts import render, redirect
from .models import Electrodomestico
from django.contrib import messages

# Create your views here.

def home(request):
    electrodomesticos = Electrodomestico.objects.all()
    messages.success(request, 'Electrodomestico listado')
    return render(request, "gestionElectrodomesticos.html", {'electrodomesticos': electrodomesticos})


def registrarElectrodomestico(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    consumo=request.POST['numConsumo']

    electrodomestico=Electrodomestico.objects.create(codigo=codigo, nombre=nombre, consumo=consumo)
    messages.success(request, 'Electrodomestico registrado')
    return redirect('/')

def edicionElectrodomestico(request, codigo):
    electrodomestico = Electrodomestico.objects.get(codigo=codigo)
    return render(request, "edicionElectrodomestico.html", {"electrodomestico": electrodomestico})

def editarElectrodomestico(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    consumo=request.POST['numConsumo']

    electrodomestico = Electrodomestico.objects.get(codigo=codigo)
    electrodomestico.nombre = nombre
    electrodomestico.consumo = consumo
    electrodomestico.save()

    messages.success(request, 'Electrodomestico modificado')

    return redirect('/')

def eliminacionElectrodomestico(request, codigo):
    electrodomestico = Electrodomestico.objects.get(codigo=codigo)
    electrodomestico.delete()

    messages.success(request, 'Electrodomestico eliminado')

    return redirect('/')