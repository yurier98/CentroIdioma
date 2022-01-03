from django.db import models




class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    cant_pc = models.IntegerField(default=1)
    disponibilidad = models.BooleanField("Disponibilidad", default=True)

    class Meta:
        # ordering = ["id"]
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

    def __str__(self) -> str:
        return str(self.nombre)


class Maquina(models.Model):
    ESTADO = (
        ('d', 'Disponible'),
        ('o', 'Ocupada'),
        ('r', 'Rota'),
    )
    id_maquina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    num_inv = models.CharField("Inventario", max_length=20)
    estado = models.CharField(max_length=1, choices=ESTADO, default='d')
    local = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Maquina"
        verbose_name_plural = "Maquinas"

    def __str__(self) -> str:
        return str(self.nombre)


class Material(models.Model):
    TIPO = (
        ('mp3', 'Audio'),
        ('doc', 'Documento'),
        ('img', 'Imagenes'),
        ('mov', 'Video'),
    )
    id_material = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO, help_text="Seleccione el tipo de material")
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(help_text="Ingrese una breve descripción del material")
    url = models.URLField()
    idioma = models.CharField(max_length=100, default='Ingles')

    def __str__(self) -> str:
        return str(self.nombre)

    class Meta:
        # ordering = ["id"]
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
