# Generated by Django 3.1.3 on 2020-12-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionLab', '0002_remove_laboratorio_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='cant_pc',
            field=models.IntegerField(default=1),
        ),
    ]