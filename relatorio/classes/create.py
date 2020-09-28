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
            obj_exams = Exame(numero_guia_consulta=Consulta.objects.get(numero_guia=new_item[0]), exame=new_item[1],
                              valor_exame=new_item[2])
            print(obj_exams)
            exams.append(obj_exams)
        Exame.objects.bulk_create(exams, batch_size=1000)


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
            new_item = item.split(';')
            obj_medico = Medico(codigo_medico=new_item[1], nome=new_item[2])
            medico.append(obj_medico)

        try:
            Medico.objects.bulk_create(medico, batch_size=1000, ignore_conflicts=True)
        except IntegrityError:
            Medico.objects.bulk_update(medico, ['nome'], batch_size=1000)

        for item in self.data_appointment[1:]:
            new_item = item.split(';')
            obj_appointment = Consulta(numero_guia=int(new_item[0]), data_consulta=new_item[3],
                                       valor_consulta=new_item[4],
                                       codigo_medico=Medico.objects.get(codigo_medico=int(new_item[1])))
            appointment.append(obj_appointment)

        try:
            Consulta.objects.bulk_create(appointment)
        except IntegrityError:
            Consulta.objects.bulk_update(appointment, ['valor_consulta'], batch_size=1000)
