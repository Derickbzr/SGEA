from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from .models import Inscricao

@login_required
def inscrever(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    Inscricao.objects.get_or_create(usuario=request.user, evento=evento)
    return redirect('listar_eventos')
