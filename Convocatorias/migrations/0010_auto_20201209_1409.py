# Generated by Django 3.1.3 on 2020-12-09 19:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Convocatorias', '0009_auto_20201204_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocatoria',
            name='body',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='estado',
            field=models.CharField(choices=[('B', 'En borrador'), ('P', 'Publicado'), ('D', 'Eliminado')], max_length=1),
        ),
    ]