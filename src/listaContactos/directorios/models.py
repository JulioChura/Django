from django.db import models

class Directorio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    informacion_contacto = models.TextField()

    def __str__(self):
        return self.nombre
