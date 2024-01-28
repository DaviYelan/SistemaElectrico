from django.urls import path
from . import views
from .views import colaboradores

urlpatterns = [
    path('', views.home),
    path('registrarElectrodomestico/', views.registrarElectrodomestico),
    path('edicionElectrodomestico/<codigo>', views.edicionElectrodomestico),
    path('editarElectrodomestico/', views.editarElectrodomestico),
    path('eliminacionElectrodomestico/<codigo>', views.eliminacionElectrodomestico),
    path('colaboradores/', colaboradores, name='colaboradores')
]