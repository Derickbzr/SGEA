from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('eventos/', include('eventos.urls')),
    path('inscricoes/', include('inscricoes.urls')),
    path("historico/", include("logs.urls")),
    path('certificados/', include('certificados.urls')),
    path("api/", include("api.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)