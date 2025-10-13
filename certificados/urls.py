from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_certificados, name='listar_certificados'),
    path('emitir/', views.emitir_certificado, name='emitir_certificado'),
]
