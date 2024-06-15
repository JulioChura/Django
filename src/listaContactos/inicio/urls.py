from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView


urlpatterns = [
    path('admin/', admin.site.urls)
]