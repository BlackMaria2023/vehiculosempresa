# Generated by Django 4.2 on 2024-04-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='year',
            field=models.IntegerField(),
        ),
    ]
