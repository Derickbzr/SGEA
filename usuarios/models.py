from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    username = None
    PERFIL_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('ORGANIZADOR', 'Organizador'),
    ]

    telefone = models.CharField(max_length=20, blank=True, null=True)
    instituicao = models.CharField(max_length=100, blank=True, null=True)
    perfil = models.CharField(max_length=15, choices=PERFIL_CHOICES, default='ALUNO')

    # Agora é o campo usado para login
    email = models.EmailField(unique=True, blank=False, null=False)

    # LOGIN será por EMAIL
    USERNAME_FIELD = "email"

    # Campos adicionais obrigatórios ao criar superuser
    # IMPORTANTE: username PRECISA estar aqui, caso contrário Django reclama.
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.perfil})"
