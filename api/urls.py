from django.urls import path
from .views import EventoListAPI, InscricaoAPI

urlpatterns = [
    path("eventos/", EventoListAPI.as_view()),
    path("eventos/<int:id>/inscrever/", InscricaoAPI.as_view()),
]