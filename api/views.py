from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def calcular_descuento_energetico(request):
    if request.method == 'GET':
        kilovatios = float(request.GET.get('kilovatios', 0))
        num_paneles_solares = int(request.GET.get('paneles_solares', 0))
        num_paneles_eolicos = int(request.GET.get('paneles_eolicos', 0))

        descuento = num_paneles_solares * 0.1 + num_paneles_eolicos * 0.05

        return JsonResponse({'descuento': descuento})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)