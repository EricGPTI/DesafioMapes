from django.contrib import messages
from django.shortcuts import render
from relatorio.classes.create import CreateDataExams, CreateDataAppointment
from relatorio.classes.prepare_data import SaveData
from relatorio.classes import relatorio


def home(request):
    return render(request, 'index.html')


def send(request):
    return render(request, 'send.html')


def filtro_reports(request):
    medicos = relatorio.get_medicos()
    return render(request, 'report.html', {'medicos': medicos})

def report(request):
    if request.method == 'POST' and request.POST:
        medico = request.POST['medico']
        data_inicio = request.POST['data_inicio']
        data_fim = request.POST['data_fim']




def file(request):
    """
    Faz a recepção de arquivos para validação dos dados e salvamento em banco.
    """
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.lower() in ['exames.csv', 'consultas.csv']:
            data = SaveData(file)
            processed_data = data.reader.type_file()
            if processed_data[0] is 'exams':
                creator = CreateDataExams(processed_data[1])
                creator.create_exams()
            else:
                creator = CreateDataAppointment(processed_data[1])
                creator.create_appointment()
            messages.info(request, 'Arquivo processado!')
            return render(request, 'send.html')
        else:
            messages.warning(request, 'Arquivo diferente do requisitado.')
            messages.warning(request, 'Verifique o nome e a extensão do arquivo.')
    return render(request, 'send.html')
