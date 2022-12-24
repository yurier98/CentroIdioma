from django.contrib import admin

# Register your models here.
from .models import Convocatoria, Inscripcion


# def Cambiarestado():


class ConvocatoriasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'fechaCreada', 'fue_publicado_reciente')
    list_filter = ['fechaCreada', 'autor']
    search_fields = ['titulo']


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ( 'fecha', 'lugar', 'disponibilidad', 'convocatoria')
    list_filter = ['fecha', 'convocatoria']
    search_fields = ['lugar']
    ordering = ['fecha']

admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Convocatoria, ConvocatoriasAdmin)
