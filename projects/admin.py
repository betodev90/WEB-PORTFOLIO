from django.contrib import admin
from .models import Proyecto # Importar el modelo Proyecto

# admin.site.register(Proyecto)

class ProyectoAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'descripcion', 'fecha_creacion', 
        'fecha_modificacion'
    ]
    search_fields = [
        'dispositivo__name',
    ]
    list_filter = ('fecha_creacion',)
admin.site.register(Proyecto, ProyectoAdmin)

