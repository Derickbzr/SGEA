from django.urls import path
from . import views

urlpatterns = [
    path('<int:evento_id>/inscrever/', views.inscrever, name='inscrever_evento'),
path('<int:evento_id>/cancelar/', views.cancelar_inscricao, name='cancelar_inscricao'),
]
