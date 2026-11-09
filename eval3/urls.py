from django.contrib import admin
from django.urls import path

from mascotas import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #responsable
    path('responsable/crear', views.crear_responsable),
    path('responsables', views.listar_responsable),
    path('responsable/modificar/<int:id>', views.modificar_responsable),
    path('responsable/eliminar/<int:id>', views.eliminar_responsable),

    #mascota
    path('mascota/crear', views.crear_mascota),
    path('mascotas', views.listar_mascotas),
    path('mascota/modificar/<int:id>', views.modificar_mascota),
    path('mascota/eliminar/<int:id>', views.eliminar_mascota),
]