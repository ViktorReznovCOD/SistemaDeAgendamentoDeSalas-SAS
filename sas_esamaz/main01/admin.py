from django.contrib import admin
from main01.models import Professor, Tipo_De_Sala, Salas, Periodo, TabelaDeAgendamento
# Register your models here.
admin.site.register(Professor)
admin.site.register(Tipo_De_Sala)
admin.site.register(Salas)
admin.site.register(Periodo)
admin.site.register(TabelaDeAgendamento)