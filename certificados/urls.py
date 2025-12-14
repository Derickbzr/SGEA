from django.urls import path
from . import views
from django.urls import path
from .views import baixar_certificado_exemplo

urlpatterns = [
    path('', views.listar_certificados, name='listar_certificados'),
    path('emitir/', views.emitir_certificado, name='emitir_certificado'),
    path("baixar-exemplo/", baixar_certificado_exemplo, name="baixar_certificado_exemplo"),
]
