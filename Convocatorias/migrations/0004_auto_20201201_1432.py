# Generated by Django 3.1.3 on 2020-12-01 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Convocatorias', '0003_auto_20201201_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convocatoria',
            name='body',
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='fechaCreada',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 19, 32, 6, 682132, tzinfo=utc), verbose_name='Fecha Creada'),
        ),
    ]
