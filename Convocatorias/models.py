import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now
from tinymce.models import HTMLField


class Convocatoria(models.Model):
    ESTADO = (
        ('B', 'En borrador'),
        ('P', 'Publicado'),
        ('D', 'Eliminado'),
    )
    id_convocatoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField("Título", max_length=100)
    img = ImageField(upload_to='static\media', default='null')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fechaCreada = models.DateTimeField('Fecha de creada', blank=False, null=False, auto_now_add=True)
    body = HTMLField("Contenido", null=True)
    estado = models.CharField("Estado", max_length=1, choices=ESTADO, default='B')

    class Meta:
        # ordering = ["id"]
        verbose_name = "Convocatoria"
        verbose_name_plural = "Convocatorias"

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        verificar si da error es q tengo q dirijirlo a detail
        """
        return reverse('convocatorias:convocatoria_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return str(self.titulo)

    def fue_publicado_reciente(self):
        return self.fechaCreada.date() >= timezone.now().date() - datetime.timedelta(days=1)

    fue_publicado_reciente.boolean = True
    # fue_publicado_reciente.descripcion_corta = 'Publicado hoy ?'


class Inscripcion(models.Model):
    id_inscripcion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField('Fecha de la Inscripción', blank=False, null=False, default=now)
    lugar = models.CharField("Lugar de la Inscripción", max_length=100)
    disponibilidad = models.IntegerField(help_text='Cantidad de usuarios que se pueden inscribir')
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(User)

    class Meta:
        # ordering = ["id"]
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        # fecha_str = "14/07/2014"
        # date_object = datetime.strptime(fecha_str, '%dd/%mm/%Y')
        #  return self.fecha.strptime(date_object, '%dd/%mm/%Y')
        return self.convocatoria.__str__()

    # Metodo para comprobar q haya disponibilidad para poder inscribirse
    def save(self, *args, **kwargs):

        cant_user_inscritos = Inscripcion.estudiantes.all().count()

        if self.disponibilidad >= cant_user_inscritos:
            return  # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.
