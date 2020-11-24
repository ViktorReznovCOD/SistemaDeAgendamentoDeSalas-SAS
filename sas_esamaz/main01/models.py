from django.db import models

# Create your models here.
class Professor(models.Model):
    ID = models.CharField(auto_created=True ,max_length=6, primary_key=True)
    NOME = models.CharField(max_length=30)

class Tipo_De_Sala(models.Model):
    ID = models.CharField(max_length=30)
    NOME = models.CharField(max_length=30)

class Salas(models.Model):
    CHOICE = [(1,'Ocupado'),(2,'Disponível')]
    ID = models.CharField(auto_created=True ,max_length=6, primary_key=True)
    NOME = models.CharField(max_length=30)
    #FK_TIPO_SALAS = models.ForeignKey ( )
    STATUS = models.BooleanField(choices=CHOICE,default=1, blank=False)

class Periodo(models.Model):
    ID = models.CharField(auto_created=True ,max_length=6, primary_key=True)
    NOME = models.CharField(max_length=30)
    #INICIO =
    #TERMINO =

class TabelaDeAgendamento (models.Model):
    CHOICE = [(1,'Sim'), (2,'Não')]
    ID = models.CharField(auto_created=True ,max_length=6, primary_key=True)
    DATA_CRIACAO = models.DateTimeField(auto_now=True)
    OBSERVAÇÃO = models.CharField(max_length=175)
    #STATUS = BOOLEANO
    #FK_SALAS = models.ForeignKey(Salas)
    #FK_PERIODOS = models.ForeignKey(Periodo)
    #FK_PROFESSOR = models.ForeignKey(Professor)
    CAIXA_DE_SOM = models.BooleanField(choices=CHOICE,blank=True)
