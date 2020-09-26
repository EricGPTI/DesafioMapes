from django.contrib import messages
from django.shortcuts import render
from relatorio.classes.reader import Reader
from relatorio.classes.save_data import SaveData
from relatorio.classes.valida_hash_file import ValidaHash


def home(request):
    return render(request, 'index.html')


def send(request):
    return render(request, 'send.html')


def report(request):
    return render(request, 'report.html')


def file(request):
    """
    Faz a recepção de arquivos para validação dos dados e salvamento em banco.
    """
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.lower() in ['exames.csv', 'consultas.csv']:
            data = SaveData(file)
            processed_data = data.reader.type_file()
            data.create(processed_data)
            # Precisa validar a partir daqui.

            return render(request, 'send.html')
        else:
            messages.warning(request, 'Arquivo diferente do requisitado.')
            messages.warning(request, 'Verifique o nome e a extensão do arquivo.')
    return render(request, 'send.html')
