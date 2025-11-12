from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from productos.models import Producto
import os

class Command(BaseCommand):
    help = 'Enlaza las imágenes en media/productos/ con los productos de la BD'

    def handle(self, *args, **options):
        # Mapeo de nombres de productos con nombres de archivos
        mapeo = {
            'lavadora': 'lavadora.webp',
            'aspiradora': 'aspiradora.webp',
            'hervidor de vidrio': 'hervidor1.webp',
            'hervidor eléctrico': 'hervidor2.webp',
        }

        media_path = 'media/productos/'
        
        for producto in Producto.objects.all():
            nombre_lower = producto.nombre.lower()
            
            # Buscar coincidencia en el mapeo
            imagen_archivo = None
            for clave, archivo in mapeo.items():
                if clave in nombre_lower:
                    imagen_archivo = archivo
                    break
            
            if imagen_archivo:
                ruta_completa = os.path.join(media_path, imagen_archivo)
                
                if os.path.exists(ruta_completa):
                    # Leer el archivo
                    with open(ruta_completa, 'rb') as f:
                        contenido = f.read()
                    
                    # Asignar la imagen al producto
                    producto.imagen.save(imagen_archivo, ContentFile(contenido), save=True)
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ {producto.nombre} <- {imagen_archivo}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'⚠ Imagen no encontrada: {ruta_completa}')
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ No hay mapeo para: {producto.nombre}')
                )

        self.stdout.write(self.style.SUCCESS('✓ ¡Proceso completado!'))
