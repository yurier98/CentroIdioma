# Generated by Django 3.2.9 on 2022-02-13 16:26

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('GestionLab', '0002_auto_20211225_1650'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id_reservacion',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('laboratorio',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionLab.laboratorio')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionLab.maquina')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reservación',
                'verbose_name_plural': 'Reservaciones',
                'ordering': ['fecha'],
            },
        ),
    ]
