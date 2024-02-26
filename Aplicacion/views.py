from django.shortcuts import render, redirect, get_object_or_404, reverse
from Aplicacion.models import Electrodomestico
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

#Redireccionamientos a las interfaces
def paginaPrincipal(request):
    return render(request, 'principal.html') 

def carrito_de_compras(request):
    return render(request, 'carrito.html')

def colaboradores(request):
    return render(request, 'colaborador.html')

def solicitar(request):
    return render(request, 'solicitar.html')

def electros(request):
    return render(request, 'electro.html')

def infos(request):
    return render(request, 'info.html')

def electrosingles(request):
    return render(request, 'electro-single.html')

def teslas(request):
    return render(request, 'tesla.html')

def sesions(request):
    return render(request, 'sesion.html')

#Funciones del sistema
def agregar_al_carrito(request, electrodomestico_codigo):
    electrodomestico = get_object_or_404(Electrodomestico, codigo=electrodomestico_codigo)
    carrito_de_compras = request.session.get('carrito_de_compras', [])
    carrito_de_compras.append(electrodomestico_codigo)
    request.session['carrito_de_compras'] = carrito_de_compras
    return redirect(reverse('carrito') + f'?added={electrodomestico_codigo}')

def eliminar_del_carrito(request, electrodomestico_codigo):
    electrodomestico = get_object_or_404(Electrodomestico, codigo=electrodomestico_codigo)
    carrito_de_compras = request.session.get('carrito_de_compras', [])
    if electrodomestico_codigo in carrito_de_compras:
        carrito_de_compras.remove(electrodomestico_codigo)
    request.session['carrito_de_compras'] = carrito_de_compras
    return redirect('carrito')

def carrito_de_compras(request):
    carrito_de_compras = request.session.get('carrito_de_compras', [])
    electrodomesticos_en_carrito = Electrodomestico.objects.filter(codigo__in=carrito_de_compras)
    return render(request, 'carrito.html', {'electrodomesticos_en_carrito': electrodomesticos_en_carrito})

def listar_electrodomesticos(request):
    electrodomesticos = Electrodomestico.objects.all()
    return render(request, 'electrodomesticos.html', {'electrodomesticos': electrodomesticos})




def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data[("password1")])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="principal")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)