from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import registro, calculos, perfiles, cambiar_contraseña_view
from api.views import calcular_descuento_energetico

urlpatterns = [
    path('', views.paginaPrincipal, name='principal'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('carrito/', views.carrito_de_compras, name='carrito'),
    path('solicitar/', views.solicitar, name='solicitar'),
    path('electrodomesticos/', views.listar_electrodomesticos, name='electrodomesticos'),
    path('infos/', views.infos, name='infos'),
    path('electros/', views.electros, name='electros'),
    path('electrosingles/', views.electrosingles, name='electrosingles'),
    path('teslas/', views.teslas, name='teslas'),
    path('sesions/', views.sesions, name='sesions'),
    path('agregar-al-carrito/<str:electrodomestico_codigo>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<str:electrodomestico_codigo>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('registro/', registro, name='registro'),
    path('calculos/', calculos, name='calculos'),
    path('perfiles/', perfiles, name='perfiles'),
    path('cambiar_contraseña/', cambiar_contraseña_view, name='cambiar_contraseña'),
    path('api/calcular_descuento_energetico/', calcular_descuento_energetico, name='calcular_descuento_energetico'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)