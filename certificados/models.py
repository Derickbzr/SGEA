from django.db import models
from usuarios.models import Usuario
from eventos.models import Evento

class Certificado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='certificados/', null=True, blank=True)
