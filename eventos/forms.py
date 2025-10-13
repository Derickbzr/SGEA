from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['tipo', 'nome', 'data_inicial', 'data_final', 'horario', 'local', 'vagas']
