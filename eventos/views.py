from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from eventos.models import Evento
from eventos.forms import EventoForm  # <-- AQUI!
from inscricoes.models import Inscricao
from logs.utils import registrar_acao


@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()

    return render(request, "eventos/listar.html", {
        "eventos": eventos
    })
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

            # Registrar ação APENAS depois de salvar o evento
            registrar_acao(
                request.user,
                "Criou evento",
                f"Nome: {evento.nome}"
            )

            messages.success(request, "Evento criado com sucesso!")
            return redirect('listar_eventos')

        else:
            messages.error(request, "Erro ao criar evento. Verifique os dados.")

    else:
        form = EventoForm()

    return render(request, "eventos/criar.html", {"form": form})

def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    # Somente organizadores podem excluir
    if request.user.perfil != "ORGANIZADOR":
        messages.error(request, "Apenas organizadores podem excluir eventos.")
        return redirect('listar_eventos')

    # Só pode excluir se for o dono
    if evento.organizador != request.user:
        messages.error(request, "Você não tem permissão para excluir este evento.")
        return redirect('listar_eventos')

    nome_evento = evento.nome
    evento.delete()

    # Registrar ação
    registrar_acao(
        request.user,
        "Excluiu evento",
        f"Nome: {nome_evento}"
    )

    messages.success(request, "Evento excluído com sucesso.")
    return redirect('listar_eventos')