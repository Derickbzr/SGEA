from django.shortcuts import render
from .models import LogAcao
from django.contrib.auth.decorators import login_required

@login_required
def historico_acoes(request):
    logs = LogAcao.objects.filter(usuario=request.user).order_by("-data")

    return render(request, "logs/historico.html", {
        "logs": logs
    })
