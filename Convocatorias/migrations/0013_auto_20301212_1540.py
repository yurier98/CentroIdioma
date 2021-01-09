# Generated by Django 3.1.3 on 2030-12-12 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Convocatorias', '0012_convocatoria_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convocatoria',
            name='autor',
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
