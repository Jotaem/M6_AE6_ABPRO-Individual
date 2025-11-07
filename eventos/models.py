from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_organizados')
    asistentes = models.ManyToManyField(User, related_name='eventos_asistidos', blank=True)

    def __str__(self):
        return self.nombre

