# Generated by Django 4.0.2 on 2022-05-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Conductor', '0004_remove_entrega_envios_remove_entrega_observacion'),
        ('Call', '0007_alter_envioguia_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='envioguia',
            name='entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrega', to='Conductor.entrega'),
        ),
        migrations.AddField(
            model_name='envioguia',
            name='observacion',
            field=models.TextField(default=''),
        ),
    ]
