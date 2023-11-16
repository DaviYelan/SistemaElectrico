from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarElectrodomestico/', views.registrarElectrodomestico),
    path('edicionElectrodomestico/<codigo>', views.edicionElectrodomestico),
    path('editarElectrodomestico/', views.editarElectrodomestico),
    path('eliminacionElectrodomestico/<codigo>', views.eliminacionElectrodomestico)
]