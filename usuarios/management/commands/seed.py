from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = [
            ("organizador@sgea.com", "Admin@123", "Organizador"),
            ("aluno@sgea.com", "Aluno@123", "Aluno"),
            ("professor@sgea.com", "Professor@123", "Professor")
        ]

        for email, senha, grupo in users:
            if not User.objects.filter(username=email).exists():
                u = User.objects.create_user(username=email, email=email, password=senha)
                u.groups.add(Group.objects.get(name=grupo))
                u.save()

        print("Seeds criados com sucesso.")
