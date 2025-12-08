from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.core.exceptions import ValidationError
import re


# --------------------------------------------
# 1. Validação de senha forte
# --------------------------------------------
def validar_senha_forte(value):
    if len(value) < 8:
        raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r"[A-Z]", value):
        raise ValidationError("A senha deve conter letra maiúscula.")
    if not re.search(r"[0-9]", value):
        raise ValidationError("A senha deve conter número.")
    if not re.search(r"[@$!%*#?&]", value):
        raise ValidationError("A senha deve conter caractere especial.")


# --------------------------------------------
# 2. FORMULÁRIO DE CADASTRO (SEM USERNAME)
# --------------------------------------------
class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        validators=[validar_senha_forte]
    )

    class Meta:
        model = Usuario
        fields = [
            'email', 'first_name', 'last_name',
            'telefone', 'instituicao', 'perfil',
            'password1', 'password2'
        ]   # <-- Note que username foi removido!

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔥 REMOVER username do form herdado
        if "username" in self.fields:
            del self.fields["username"]

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
        return email


# --------------------------------------------
# 3. Login usando email
# --------------------------------------------
class LoginUsuarioForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail")  # <-- agora login é por email
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
