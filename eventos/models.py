from django.db import models

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from django.apps import apps


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
    organizador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='eventos_organizados',
        limit_choices_to={'groups__name': 'Professor'},
        null=True,
        blank=True
    )
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='eventos_responsaveis',
        limit_choices_to={'groups__name': 'Professor'},
        null=True,
        blank=True
    )

    banner = models.ImageField(upload_to="banners/", null=True, blank=True)




    def __str__(self):
        return f"{self.nome} - {self.tipo}"

    def clean(self):
        # Só valida se as duas datas existirem
        if self.data_inicial and self.data_inicial < timezone.localdate():
            raise ValidationError("A data inicial não pode ser no passado.")

        if self.data_inicial and self.data_final and self.data_final < self.data_inicial:
            raise ValidationError("A data final deve ser após o início.")
    def inscrever(self, usuario):
        Inscricao = apps.get_model('inscricoes', 'Inscricao')

        if Inscricao.objects.filter(evento=self, usuario=usuario).exists():
            raise Exception("Usuário já inscrito.")

        if self.inscricao_set.count() >= self.vagas:
            raise Exception("Limite de vagas atingido.")

        Inscricao.objects.create(evento=self, usuario=usuario)