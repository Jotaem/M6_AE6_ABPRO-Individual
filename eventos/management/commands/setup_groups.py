
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from eventos.models import Evento

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios y asigna los permisos iniciales.'

    def handle(self, *args, **options):
        # Obtener el content type para el modelo Evento
        content_type = ContentType.objects.get_for_model(Evento)

        # Permisos
        add_evento_perm = Permission.objects.get(codename='add_evento', content_type=content_type)
        change_evento_perm = Permission.objects.get(codename='change_evento', content_type=content_type)
        delete_evento_perm = Permission.objects.get(codename='delete_evento', content_type=content_type)
        view_evento_perm = Permission.objects.get(codename='view_evento', content_type=content_type)

        # Grupo de Administradores
        admin_group, created = Group.objects.get_or_create(name='Administradores')
        if created:
            admin_group.permissions.add(add_evento_perm, change_evento_perm, delete_evento_perm, view_evento_perm)
            self.stdout.write(self.style.SUCCESS('Grupo "Administradores" creado y con permisos.'))
        else:
            self.stdout.write('Grupo "Administradores" ya existe.')

        # Grupo de Organizadores de eventos
        organizador_group, created = Group.objects.get_or_create(name='Organizadores de eventos')
        if created:
            organizador_group.permissions.add(add_evento_perm, change_evento_perm, view_evento_perm)
            self.stdout.write(self.style.SUCCESS('Grupo "Organizadores de eventos" creado y con permisos.'))
        else:
            self.stdout.write('Grupo "Organizadores de eventos" ya existe.')

        # Grupo de Asistentes
        asistente_group, created = Group.objects.get_or_create(name='Asistentes')
        if created:
            asistente_group.permissions.add(view_evento_perm)
            self.stdout.write(self.style.SUCCESS('Grupo "Asistentes" creado y con permisos.'))
        else:
            self.stdout.write('Grupo "Asistentes" ya existe.')
