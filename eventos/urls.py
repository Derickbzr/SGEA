from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('novo/', views.criar_evento, name='criar_evento'),
]
