from django.shortcuts import render, redirect
from django.http import FileResponse
from certificados.models import Certificado
import os
from django.conf import settings
from eventos.models import Evento


def listar_certificados(request):
    certificados = [
        {"usuario": "Derick Bezerra", "evento": "Semana de Tecnologia", "data": "2024-11-12"},
        {"usuario": "Derick Bezerra", "evento": "Palestra de IA", "data": "2024-10-02"},
    ]

    return render(request, 'certificados/listar.html', {
        "certificados": certificados
    })

def emitir_certificado(request):
    if request.method == 'POST':
        usuario_nome = request.POST.get("usuario")
        evento_nome = request.POST.get("evento")
        data = request.POST.get("data")
        registrar_acao(request.user, "Emitiu certificado", f"Evento: {evento_nome}")

        # Encontrar evento pelo nome
        try:
            evento = Evento.objects.get(nome__iexact=evento_nome.strip())
        except Evento.DoesNotExist:
            return render(request, 'certificados/emitir.html', {
                "erro": "Evento não encontrado. Verifique o nome digitado."
            })

        # Criar certificado corretamente
        Certificado.objects.create(
            usuario=request.user,
            evento=evento,
            data=data
        )

        return redirect('listar_certificados')

    return render(request, 'certificados/emitir.html')

def baixar_certificado_exemplo(request):
    caminho_pdf = os.path.join(settings.BASE_DIR, "static", "pdf", "certificado_exemplo.pdf")

    return FileResponse(open(caminho_pdf, "rb"), content_type='application/pdf')