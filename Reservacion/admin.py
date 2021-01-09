from django.contrib import admin

# Register your models here.
from .models import Reservacion


class ReservacionesAdmin(admin.ModelAdmin):
    list_display = ('fecha','local','maquina')
    list_filter = ['local','fecha']

admin.site.register(Reservacion,ReservacionesAdmin)
