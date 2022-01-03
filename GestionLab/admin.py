from django.contrib import admin

# Register your models here.
from .models import Laboratorio, Maquina, Material


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'cant_pc', 'disponibilidad')
    list_filter = ['ubicacion', 'disponibilidad']


class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'local', 'num_inv', 'estado')
    list_filter = ['local', 'estado']


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id_material', 'nombre', 'idioma', 'tipo', 'autor', 'url')
    list_filter = ['tipo']


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Material, MaterialAdmin)
