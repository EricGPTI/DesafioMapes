from django.contrib import messages
from django.shortcuts import render
from relatorio.classes.reader import Reader
from relatorio.classes.valida_hash_file import ValidaHash


def home(request):
    return render(request, 'index.html')


def send(request):
    return render(request, 'send.html')


def report(request):
    return render(request, 'report.html')


def file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.lower() in ['exames.csv', 'consultas.csv']:
            valida_hash = ValidaHash(file)
            print(valida_hash.compare_hase())

            data = Reader(file)

            print(data.process_exames())

            return render(request, 'send.html')
        else:
            messages.warning(request, 'Arquivo diferente do requisitado.')
            messages.warning(request, 'Verifique o nome e a extensão do arquivo.')
    return render(request, 'send.html')
