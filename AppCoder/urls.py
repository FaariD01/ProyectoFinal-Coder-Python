from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("edificios/", views.edificios, name='Edificios'),
    path('equipo/', views.equipo, name="Equipo"),
    path('edificiosApi/', views.edificiosapi),
    path('equipoApi/', views.equipoapi),
    path('encargados/', views.encargados, name="Encargados"),
    path('encargadoApi/', views.encargadoapi),
    path("busquedaEdificio/", views.buscaredificio, name="BusquedaEdificio"),
    path("buscar/", views.buscar)



]
