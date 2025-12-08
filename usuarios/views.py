from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CadastroUsuarioForm, LoginUsuarioForm
from django.core.mail import send_mail

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            return redirect('login')
        else:
            print("ERROS NO CADASTRO:", form.errors)  # DEBUG IMPORTANTE

    else:
        form = CadastroUsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_eventos')
    else:
        form = LoginUsuarioForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')

def enviar_confirmacao(user):
    link = f"http://localhost:8000/confirmar/{user.pk}/"
    send_mail(
        "Confirme seu cadastro no SGEA",
        f"Olá {user.first_name}, confirme seu cadastro: {link}",
        "no-reply@sgea.com",
        [user.email]
    )
