# Generated by Django 4.0.2 on 2022-04-21 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Vehiculos', '0002_remove_tipovehiculo_descripcion_tipovehiculo_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EnvioGuia', to=settings.AUTH_USER_MODEL),
        ),
    ]
