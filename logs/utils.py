from .models import LogAcao

def registrar_acao(usuario, acao, detalhes=None):
    if usuario.is_authenticated:
        LogAcao.objects.create(
            usuario=usuario,
            acao=acao,
            detalhes=detalhes
        )
