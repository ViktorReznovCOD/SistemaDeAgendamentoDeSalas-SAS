# Generated by Django 3.1.3 on 2020-11-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('ID', models.CharField(auto_created=True, max_length=6, primary_key=True, serialize=False)),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('ID', models.CharField(auto_created=True, max_length=6, primary_key=True, serialize=False)),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('ID', models.CharField(auto_created=True, max_length=6, primary_key=True, serialize=False)),
                ('NOME', models.CharField(max_length=30)),
                ('STATUS', models.BooleanField(choices=[(1, 'Ocupado'), (2, 'Disponível')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TabelaDeAgendamento',
            fields=[
                ('ID', models.CharField(auto_created=True, max_length=6, primary_key=True, serialize=False)),
                ('DATA_CRIACAO', models.DateTimeField(auto_now=True)),
                ('OBSERVAÇÃO', models.CharField(max_length=175)),
                ('CAIXA_DE_SOM', models.BooleanField(blank=True, choices=[(1, 'Sim'), (2, 'Não')])),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_De_Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=30)),
                ('NOME', models.CharField(max_length=30)),
            ],
        ),
    ]