from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Professor(models.Model):
    NOME = models.CharField(max_length=30)
    def __str__(self):
        return self.NOME

class Turma:
    NOME = models.CharField(max_length=30)
    def __str__(self):
        return self.NOME

class Tipo_De_Sala(models.Model):
    NOME = models.CharField(max_length=30)
    def __str__(self):
        return self.NOME

class Salas(models.Model):
    CHOICE = [(1,'Ocupado'),(2,'Disponível')]
    NOME = models.CharField(max_length=30)
    #FK_TIPO_SALA = models.ForeignKey (Tipo_De_Sala, on_delete=models.CASCADE)
    STATUS = models.BooleanField(choices=CHOICE,default=1, blank=False)
    def __str__(self):
        return self.NOME

class Periodo(models.Model):
    NOME = models.CharField(max_length=30)
    #INICIO =
    #TERMINO =
    def __str__(self):
        return self.NOME

class TabelaDeAgendamento (models.Model):
    CHOICE = [('Sim','sim'), ('Nao','nao')]
    #DATA_CRIACAO = models.DateTimeField(auto_now=True, default=django.utils.timezone.now)
    OBSERVACAO = models.CharField(max_length=175)
    #STATUS = BOOLEANO
    #FK_SALAS = models.ForeignKey(Salas, on_delete=models.CASCADE)
    #FK_PERIODOS = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    #FK_PROFESSOR = models.ForeignKey(Professor, on_delete=models.CASCADE)
    #CAIXA_DE_SOM = models.BooleanField(choices=CHOICE,blank=True)
    def __str__(self):
        return self.ID
