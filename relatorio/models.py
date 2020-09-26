from django.db import models


class Medico(models.Model):
    codigo_medico = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)


class Consulta(models.Model):
    numero_guia = models.IntegerField(primary_key=True)
    data_consulta = models.DateField()
    valor_consulta = models.FloatField()
    codigo_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    class META:
        ordering = ['data_consulta']


class Exame(models.Model):
    exame = models.CharField(max_length=30, null=False)
    valor_exame = models.FloatField()
    numero_guia_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    class META:
        ordering = ['-valor_exame']


class HashFile(models.Model):
    hash = models.CharField(max_length=255)
