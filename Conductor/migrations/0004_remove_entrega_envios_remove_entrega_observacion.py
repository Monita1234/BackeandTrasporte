# Generated by Django 4.0.2 on 2022-05-09 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Conductor', '0003_entrega_observacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='envios',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='observacion',
        ),
    ]
