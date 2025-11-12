from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)

    def has_delete_permission(self, request, obj=None):
        # Solo los superusuarios o usuarios en el grupo "Administradores" pueden eliminar
        if request.user.is_superuser or request.user.groups.filter(name='Administradores').exists():
            return True
        return False

admin.site.register(Producto, ProductoAdmin)