from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'teste1.html')
def testequasar(request):
    return render(request,'testequasar.html')

def visualizacao(request):
    return render(request,'visualizacao.html')

def pesquisa(request):
    return render(request,'pesquisa.html')

def agendamento(request):
    return render(request,'agendamento.html')