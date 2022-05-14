# Generated by Django 4.0.2 on 2022-05-09 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Call', '0009_remove_envioguia_entrega_and_more'),
        ('Conductor', '0004_remove_entrega_envios_remove_entrega_observacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conductor.entrega')),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Call.envioguia')),
            ],
        ),
    ]