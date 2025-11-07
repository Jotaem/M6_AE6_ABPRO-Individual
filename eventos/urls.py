from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('', views.HomeView.as_view(), name='home'),
    path('eventos/', views.ListaEventosView.as_view(), name='lista_eventos'),
    path('evento/nuevo/', views.CrearEventoView.as_view(), name='crear_evento'),
    path('evento/<int:pk>/', views.DetalleEventoView.as_view(), name='detalle_evento'),
    path('evento/<int:pk>/editar/', views.EditarEventoView.as_view(), name='editar_evento'),
    path('evento/<int:pk>/eliminar/', views.EliminarEventoView.as_view(), name='eliminar_evento'),
    path('acceso-denegado/', views.AccesoDenegadoView.as_view(), name='acceso_denegado'),
]