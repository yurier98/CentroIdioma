# Generated by Django 3.1.3 on 2020-12-01 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionLab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='question_text',
        ),
    ]
