from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from eventos.models import Evento
from .serializers import EventoSerializer


class EventoListAPI(ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]
    throttle_scope = "consulta_eventos"

class InscricaoAPI(APIView):
    permission_classes = [IsAuthenticated]
    throttle_scope = "inscricao_eventos"

    def post(self, request, id):
        evento = Evento.objects.get(pk=id)
        evento.inscrever(request.user)
        return Response({"mensagem": "Inscrição realizada"})
