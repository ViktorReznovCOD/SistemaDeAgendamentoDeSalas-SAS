from django.shortcuts import render
from .models import TabelaDeAgendamento, Tipo_De_Sala

# Create your views here.
def home(request):
    card = Tipo_De_Sala.objects.order_by('NOME')[0:]
    context = {'card':card}
    return render(request,'teste1.html',context)

def testequasar(request):
    return render(request,'teste2.html')

def visualizacao(request):
    return render(request,'visualizacao.html')

def pesquisa(request):
    return render(request,'pesquisa.html')

def agendamento(request):
    return render(request,'agendamento.html')