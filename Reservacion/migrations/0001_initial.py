# Generated by Django 3.1.3 on 2020-12-01 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GestionLab', '0006_auto_20201201_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('solapin', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionLab.laboratorio')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionLab.maquina')),
            ],
        ),
    ]