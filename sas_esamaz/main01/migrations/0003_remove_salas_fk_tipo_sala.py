# Generated by Django 3.1.3 on 2020-11-30 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main01', '0002_auto_20201130_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salas',
            name='FK_TIPO_SALA',
        ),
    ]
