from django.urls import path
from .views import historico_acoes

urlpatterns = [
    path("", historico_acoes, name="historico_acoes"),
]
