from relatorio.models import Exame, Consulta, Medico


class CreateDataExams:
    """
    Cria os dados no banco de dados a partir de um lote de dados de exames.
    """
    def __init__(self, data_exams):
        self.data_exams = data_exams

    def create(self):
        exams = []
        for item in self.data_exams:
            obj_exams = Exame(numero_guia_consulta=item[0], exame=item[1], valor_exame=item[2])
            exams.append(obj_exams)
        Exame.object.bulk_create(exams)


class CreateDataAppointment:
    """
        Cria os dados no banco de dados a partir de um lote de dados de consulta.
    """
    def __init__(self, data_appointment):
        self.data_appointment = data_appointment

    def create(self):
        appointment = []
        medico = []
        for item in self.data_appointment:
            obj_appointment = Consulta(numero_guia=item[0], data_consulta=[3], valor_consulta=item[4],
                                       codigo_medico=item[1])
            appointment.append(obj_appointment)

            obj_medico = Medico(codigo_medico=item[1], nome=item[2])
            medico.append(obj_medico)

        Consulta.object.bulk_create(appointment)

        for m in medico:
            obj = Medico.object.filter(codigo_medico=m[1])
            if obj in m:
                medico.remove(m)
        Medico.object.bulk_create(medico)




