class Reader:
    """
    Leitor de arquivos para consultas e exames.
    """
    def __init__(self, file):
        self.file = file

    def process_exams(self):
        """
        Método para processamento de exames.
        """
        for chunk in self.file.chunks(1000):
            data_exams = chunk.decode('utf-8')
            data_exams = data_exams.split('\n')
            return data_exams

    def process_appointment(self):
        """
        Método para processamento de consultas.
        """
        for chunk in self.file.chunks():
            data_appointment = chunk.decode('utf-8')
            data_appointment = data_appointment.split('\n')
            return data_appointment

    def type_file(self):
        """
        Método para verificar o nome do arquivo e faz a chamada de outro método
        para processamento e inserção no banco de dados.
        """
        if self.file.name.lower() == 'exames.csv':
            data_exams = self.process_exams()
            return 'exams', data_exams
        elif self.file.name == 'consultas.csv':
            data_appointment = self.process_appointment()
            return 'appointment', data_appointment
