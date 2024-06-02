from django.db import models

# Create your models here.

class Recordatorios(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)    