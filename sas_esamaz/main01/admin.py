from django.contrib import admin
from main01.models import Professor, Tipo_De_Sala, Salas, Periodo, TabelaDeAgendamento, Turma
# Register your models here.
admin.site.register(Professor)
admin.site.register(Tipo_De_Sala)
admin.site.register(Salas)
admin.site.register(Periodo)
admin.site.register(TabelaDeAgendamento)
admin.site.register(Turma)