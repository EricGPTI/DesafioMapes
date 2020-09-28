from relatorio.models import Exame, Consulta, Medico
from django.db import IntegrityError


class CreateDataExams:
    """
    Cria os dados no banco de dados a partir de um lote de dados de exames.
    """
    def __init__(self, data_exams):
        self.data_exams = data_exams

    def create_exams(self):
        exams = []
        del self.data_exams[-1]
        for item in self.data_exams[1:]:
            new_item = item.split(';')
            obj_exams = Exame(numero_guia_consulta=new_item[0], exame=new_item[1], valor_exame=new_item[2])
            exams.append(obj_exams)
        Exame.objects.bulk_create(exams)


class CreateDataAppointment:
    """
        Cria os dados no banco de dados a partir de um lote de dados de consulta.
    """
    def __init__(self, data_appointment):
        self.data_appointment = data_appointment

    def create_appointment(self):
        appointment = []
        medico = []
        del self.data_appointment[-1]
        for item in self.data_appointment[1:]:
            try:
                new_item = item.split(';')
                obj_medico = Medico(codigo_medico=new_item[1], nome=new_item[2])
                medico.append(obj_medico)
            except ValueError as e:
                continue


        Medico.objects.bulk_create(medico, ignore_conflicts=True)

        for item in self.data_appointment[1:]:
            new_item = item.split(';')
            guia = Consulta.objects.get(numero_guia=int(new_item[0]))
            obj_appointment = Consulta(numero_guia=int(new_item[0]), data_consulta=new_item[3],
                                       valor_consulta=new_item[4],
                                       codigo_medico=Medico.objects.get(codigo_medico=int(new_item[1])))
            appointment.append(obj_appointment)

        Consulta.objects.bulk_create(appointment)
