from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  variaveis = {
    'minha_primeira_variavel': "Hello, variáveis depois de alterar o diretório!"
  }
  return render(request, 'primeira_aplicacao/index.html', context=variaveis)
