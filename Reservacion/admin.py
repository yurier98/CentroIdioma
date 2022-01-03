from django.contrib import admin

# Register your models here.
from .models import Reservacion


class ReservacionesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'laboratorio', 'maquina')
    list_filter = ['laboratorio', 'fecha']


admin.site.register(Reservacion, ReservacionesAdmin)
