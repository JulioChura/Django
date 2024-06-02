from django.db import models

# Create your models here.

class Persona(models.Models):
    nombre = models.TextField()
    apellidos = models.TextField()
    edad = models.TextField()