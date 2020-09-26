from relatorio.models import Exame, Consulta, Medico


class CreateDataExams:
    """
    Cria os dados no banco de dados a partir de um lote de dados.
    """
    def __init__(self, data_exames):
        self.data_exames = data_exames

    def create(self):
        exams = []
        for item in self.data_exames:
            obj = Exame(numero_guia_consulta=item[0], exame=item[1], valor_exame=item[2])
            exams.append(obj)
        Exame.object.bulk_create(exams)



