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
    path("buscar/", views.buscar),
    path("leerEdificio/", views.leer_edificio),
    path("crearEdificio/", views.crear_edificio),
    path("editarEdificio/", views.editar_edificio),
    path("eliminarEdificio/", views.eliminar_edificio),
    path("edificio/list/", views.EdificioList.as_view(), name='List'),
    path("edificio/create/", views.EdificioCreate.as_view(), name='New'),
    path("edificio/edit/<pk>", views.EdificioEdit.as_view(), name='Edit'),
    path("edificio/detail/<pk>", views.EdificioDetail.as_view(), name='Detail'),
    path("edificio/delete/<pk>", views.EdificioDelete.as_view(), name='Delete'),
]
