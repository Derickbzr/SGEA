from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIL_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('ORGANIZADOR', 'Organizador'),
    ]

    telefone = models.CharField(max_length=20, blank=True, null=True)
    instituicao = models.CharField(max_length=100, blank=True, null=True)
    perfil = models.CharField(max_length=15, choices=PERFIL_CHOICES, default='ALUNO')

    def __str__(self):
        return f"{self.username} ({self.perfil})"
