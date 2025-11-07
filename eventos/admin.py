from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Evento en el panel de administración.
    """
    list_display = ('nombre', 'fecha', 'organizador')
    list_filter = ('fecha', 'organizador')
    search_fields = ('nombre', 'descripcion')
    # Permite editar el campo de asistentes directamente desde la lista de eventos
    filter_horizontal = ('asistentes',)

admin.site.register(Evento, EventoAdmin)