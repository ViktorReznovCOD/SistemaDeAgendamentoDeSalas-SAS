# Generated by Django 3.1.3 on 2020-11-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30)),
                ('STATUS', models.BooleanField(choices=[(1, 'Ocupado'), (2, 'Disponível')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TabelaDeAgendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBSERVACAO', models.CharField(max_length=175)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_De_Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
    ]
