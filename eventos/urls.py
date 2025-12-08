from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('excluir/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)