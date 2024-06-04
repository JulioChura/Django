from django.db import models
from django.http import http
# Create your models here.

def myHomeView(request):
    return http("<h1>Hola desde mi app inicio</h1>")