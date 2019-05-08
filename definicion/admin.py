# definicion/admin.py
from django.contrib import admin

from .models import Proyecto
from .forms import ProyectoChangeForm, ProyectoCreationForm
#from .views import CrearProyecto, Proyectos

class CustomProyecto(Proyecto):
    add_form = ProyectoCreationForm
    form = ProyectoChangeForm
    model = Proyecto
    list_display = ['nombre', 'fecha_inicio', 'fecha_fin', 'miembros', 'descripcion_breve', 'descripcion_detallada', 'estado']

    fieldsets = (
        (None, {'fields': ('nombre', 'fecha_inicio', 'fecha_fin', 'miembros', 'descripcion_breve', 'descripcion_detallada', 'estado')}),)

admin.site.register(CustomProyecto)