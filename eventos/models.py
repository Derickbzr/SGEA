from django.db import models
from usuarios.models import Usuario

class Evento(models.Model):
    TIPOS = [
        ('SEMINARIO', 'Seminário'),
        ('PALESTRA', 'Palestra'),
        ('MINICURSO', 'Minicurso'),
        ('SEMANA', 'Semana Acadêmica'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS)
    nome = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_final = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.tipo}"
