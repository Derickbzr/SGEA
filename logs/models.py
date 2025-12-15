from django.db import models
from django.conf import settings

class LogAcao(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    acao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.data}"
