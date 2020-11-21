from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('testequasar', views.testequasar, name='testequasar'),
    path('visualizacao', views.visualizacao, name='visualizacao'),
    path('agendamento', views.agendamento, name='agendamento'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
]