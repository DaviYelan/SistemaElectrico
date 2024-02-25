from django.urls import path
from . import views
from .views import colaboradores
from .views import plantilla
from .views import acercas
from .views import electros
from .views import infos
from .views import electrosingles
from .views import teslas
from .views import sesions

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarElectrodomestico/', views.registrarElectrodomestico),
    path('edicionElectrodomestico/<codigo>', views.edicionElectrodomestico),
    path('editarElectrodomestico/', views.editarElectrodomestico),
    path('eliminacionElectrodomestico/<codigo>', views.eliminacionElectrodomestico),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('plantilla/', plantilla, name='plantilla'),
    path('acercas/', acercas, name='acercas'),
    path('electros/', electros, name='electros'),
    path('infos/', infos, name='infos'),
    path('electrosingles/', electrosingles, name='electrosingles'),
    path('teslas/', teslas, name='teslas'),
    path('sesions/',sesions, name='sesions'),
]