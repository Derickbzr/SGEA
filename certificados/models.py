from django.db import models
from usuarios.models import Usuario
from eventos.models import Evento
from django.utils import timezone

class Certificado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)  # <-- ADICIONADO
    data_emissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.evento}"
