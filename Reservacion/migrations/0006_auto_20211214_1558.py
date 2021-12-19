# Generated by Django 3.2.9 on 2021-12-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservacion', '0005_reservacion_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservacion',
            options={'ordering': ['id'], 'verbose_name': 'Reservación', 'verbose_name_plural': 'Reservaciones'},
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hora',
            field=models.TimeField(default='00:00', verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]