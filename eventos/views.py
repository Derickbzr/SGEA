from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from eventos.models import Evento
from eventos.forms import EventoForm  # <-- AQUI!
from inscricoes.models import Inscricao

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()

    # cria uma lista de eventos com atributo calculado "vagas_restantes"
    for evento in eventos:
        evento.vagas_restantes = evento.vagas - evento.inscricao_set.count()

    inscricoes_ids = Inscricao.objects.filter(usuario=request.user).values_list("evento_id", flat=True)

    return render(request, "eventos/listar.html", {
        "eventos": eventos,
        "inscricoes_ids": inscricoes_ids
    })
@login_required
def criar_evento(request):
    if request.user.perfil != "ORGANIZADOR":
        messages.error(request, "Apenas organizadores podem criar eventos.")
        return redirect('listar_eventos')

    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            messages.success(request, "Evento criado com sucesso!")
            return redirect('listar_eventos')
    else:
        form = EventoForm()

    return render(request, "eventos/criar.html", {"form": form})

@login_required
def excluir_evento(request, evento_id):
    if request.user.perfil != "ORGANIZADOR":
        messages.error(request, "Apenas organizadores podem excluir eventos.")
        return redirect('listar_eventos')

    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, "Evento não encontrado.")
        return redirect('listar_eventos')

    evento.delete()
    messages.success(request, "Evento excluído com sucesso!")
    return redirect('listar_eventos')