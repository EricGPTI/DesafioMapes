from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def send(request):
    return render(request, 'send.html')


def file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.lower() in ['exames.csv', 'consultas.csv']:
            print(file.name)
            return render(request, 'send.html')
        else:
            messages.warning(request, 'Arquivo diferente do requisitado.')
            messages.warning(request, 'Verifique o nome e a extensão do arquivo.')
    return render(request, 'send.html')
