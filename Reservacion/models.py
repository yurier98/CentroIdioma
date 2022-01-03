import uuid

from django.contrib.auth.models import User
from django.db import models

from GestionLab.models import Laboratorio, Maquina


class Reservacion(models.Model):
    id_reservacion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    hora = models.TimeField("Hora")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(User)

    def __str__(self) -> str:
        return str(self.fecha)

    class Meta:
        ordering = ["fecha"]
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"
