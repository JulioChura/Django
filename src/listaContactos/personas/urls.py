from django.urls import path
from .views import *
app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list' ),
    path('<int:pk>/', PersonaDetailView.as_view(), name = "persona-detail"),
    path('create/', PersonaCreateView.as_view(), name="persona-create"),
    #path('anotherAdd/', personaAnotherCreateView.as_view() , name="OtroAgregarPersonas"),
    path("add/", personaCreateView, name="form-datosLlenados"),
    #path("<int:myId>/", personasShowObject, name="browsing" ),
    path('list/', personasListView, name="listing"),
    path('eliminar/<int:myID>/', personasDeleteView, name="deleting"),
    path('eliminar/', personaCreateView, name="delete"),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name='persona-update'),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete')


]
