from django.contrib import admin

# Register your models here.
from .models import Laboratorio, Maquina, Materiales


class LaboratoriosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'cant_pc', 'disponibilidad')
    list_filter = ['ubicacion', 'disponibilidad']


class MaquinasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'local', 'num_inv', 'estado')
    list_filter = ['local', 'estado']


class MaterialesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'idioma' ,'tipo', 'autor', 'url')
    list_filter = ['tipo']


admin.site.register(Laboratorio, LaboratoriosAdmin)
admin.site.register(Maquina, MaquinasAdmin)
admin.site.register(Materiales, MaterialesAdmin)
