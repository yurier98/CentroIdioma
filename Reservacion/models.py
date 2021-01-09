import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from GestionLab.models import Laboratorio, Maquina
from Convocatorias.models import Convocatoria


# def maqdelLab(lab):
#     return Maquina.local(lab)

class Reservacion(models.Model):
    fecha = models.DateTimeField("Fecha de la reservación")
    local = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(User)

    class Meta:
        ordering = ["id"]

    # def __str__(self):
    #     return self.fecha.strptime('%dd/%mm/%Y')
    # ARREGLAR ESTE FORMATO
   # @property
    # def __str__(self):
    # fecha_str = "14/07/2014"
    # date_object = datetime.strptime(fecha_str, '%dd/%mm/%Y')
    #  return self.fecha.strptime(date_object, '%dd/%mm/%Y')
    # return self.fecha.strptime('%dd/%mm/%YYYY')
    # return self.fecha.__str__()

    #  def get_absolute_url(self):

    """
    Devuelve el URL a una instancia particular de Book
    """
#   return reverse('reservacion-detail', args=[str(self.id)])

# def save(self, force_insert=False, force_update=False, using=None,
#          update_fields=None):
#
#     return
