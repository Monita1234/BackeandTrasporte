# Generated by Django 4.0.2 on 2022-05-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciosdocumentos',
            name='año',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='preciospaquetes',
            name='año',
            field=models.IntegerField(default=0),
        ),
    ]
