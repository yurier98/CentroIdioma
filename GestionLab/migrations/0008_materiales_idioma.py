# Generated by Django 3.1.3 on 2020-12-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionLab', '0007_auto_20201204_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiales',
            name='idioma',
            field=models.CharField(default='Ingles', max_length=100),
        ),
    ]
