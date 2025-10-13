from django.urls import path
from . import views

urlpatterns = [
    path('<int:evento_id>/inscrever/', views.inscrever, name='inscrever_evento'),
]
