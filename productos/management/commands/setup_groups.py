from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from productos.models import Producto

class Command(BaseCommand):
    help = 'Crea grupos, usuarios de prueba y asigna permisos para la app de productos.'

    def handle(self, *args, **options):
        self.stdout.write("Iniciando configuración de permisos y usuarios de prueba...")

        # --- 1. OBTENER CONTENT TYPE DEL MODELO PRODUCTO ---
        try:
            content_type = ContentType.objects.get_for_model(Producto)
            self.stdout.write(self.style.SUCCESS(f"Content type para '{Producto._meta.model_name}' obtenido."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al obtener ContentType para Producto: {e}"))
            return

        # --- 2. OBTENER PERMISOS ---
        try:
            add_producto_perm = Permission.objects.get(content_type=content_type, codename='add_producto')
            change_producto_perm = Permission.objects.get(content_type=content_type, codename='change_producto')
            delete_producto_perm = Permission.objects.get(content_type=content_type, codename='delete_producto')
            view_producto_perm = Permission.objects.get(content_type=content_type, codename='view_producto')
            self.stdout.write(self.style.SUCCESS("Permisos de Producto cargados."))
        except Permission.DoesNotExist:
            self.stdout.write(self.style.WARNING(
                "No se encontraron los permisos para el modelo Producto. "
                "Asegúrate de haber corrido las migraciones ('manage.py migrate') antes de ejecutar este comando."
            ))
            return

        # --- 3. CREAR GRUPOS Y ASIGNAR PERMISOS ---
        
        # Grupo de Administradores
        admin_group, created = Group.objects.get_or_create(name='Administradores')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Administradores" creado.'))
        admin_group.permissions.add(add_producto_perm, change_producto_perm, delete_producto_perm, view_producto_perm)
        
        # Grupo de Gestores de Productos
        gestor_group, created = Group.objects.get_or_create(name='Gestores de Productos')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Gestores de Productos" creado.'))
        gestor_group.permissions.add(add_producto_perm, change_producto_perm, view_producto_perm)
        
        self.stdout.write(self.style.SUCCESS("Permisos asignados a los grupos correctamente."))

        # --- 4. CREAR USUARIOS DE PRUEBA ---
        
        users_data = {
            'admin_user': {
                'password': 'adminpassword123',
                'group': admin_group,
            },
            'gestor_user': {
                'password': 'gestorpassword123',
                'group': gestor_group,
            },
            'normal_user': {
                'password': 'normalpassword123',
                'group': None, # No pertenece a un grupo con permisos de producto
            }
        }

        self.stdout.write("\n--- Creando Usuarios de Prueba ---")
        for username, data in users_data.items():
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=data['password'], email=f'{username}@example.com')
                user.is_staff = True  # Para que puedan acceder al sitio de admin
                user.save()
                
                if data['group']:
                    user.groups.add(data['group'])
                
                self.stdout.write(f"Usuario: '{username}' (Password: '{data['password']}') creado y configurado.")
            else:
                self.stdout.write(self.style.WARNING(f"Usuario '{username}' ya existe. No se ha modificado."))

        self.stdout.write(self.style.SUCCESS("\nConfiguración completada con éxito."))