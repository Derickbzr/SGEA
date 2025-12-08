from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from eventos.models import Evento
from .models import Inscricao
from certificados.utils import enviar_certificado

@login_required
def inscrever(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    total_inscritos = Inscricao.objects.filter(evento=evento).count()

    if total_inscritos >= evento.vagas:
        print("SEM VAGAS →", evento.nome)
        return redirect('listar_eventos')

    inscricao, created = Inscricao.objects.get_or_create(usuario=request.user, evento=evento)

    if created:
        print("INSCRIÇÃO REALIZADA →", request.user.username, evento.nome)
        enviar_certificado(request.user, evento)
    else:
        print("USUÁRIO JÁ INSCRITO →", request.user.username, evento.nome)

    return redirect('listar_eventos')


@login_required
def cancelar_inscricao(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    inscricao = Inscricao.objects.filter(usuario=request.user, evento=evento)

    if inscricao.exists():
        inscricao.delete()
        print("INSCRIÇÃO CANCELADA →", request.user.username, evento.nome)
    else:
        print("TENTATIVA DE CANCELAMENTO SEM INSCRIÇÃO →", request.user.username)

    return redirect('listar_eventos')
