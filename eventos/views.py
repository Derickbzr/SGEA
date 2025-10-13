from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar.html', {'eventos': eventos})

@login_required
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar.html', {'form': form})
