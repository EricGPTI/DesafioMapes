from relatorio.models import Consulta, Medico, Exame


def get_medicos():
    medicos = Medico.objects.all()
    return medicos


