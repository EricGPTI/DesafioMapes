from relatorio.classes.reader import Reader


class SaveData:
    """
    Classe para salvar dados processados.
    """

    def __init__(self, file):
        self.file = file
        self.reader = Reader(self.file)

    def process_exams(self):
        self.reader.process_exams

    def process_appointment(self):
        self.reader.process_appointment
