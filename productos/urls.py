from django.urls import path
from .views import (
    HomeView,
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    acceso_denegado,
    registro,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registro/', registro, name='registro'),
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/crear/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),
]
