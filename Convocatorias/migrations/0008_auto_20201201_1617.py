# Generated by Django 3.1.3 on 2020-12-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Convocatorias', '0007_convocatoria_fechacreada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='fechaCreada',
            field=models.DateTimeField(verbose_name='Fecha creada'),
        ),
    ]
