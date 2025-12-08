# 🎓 SGEA – Sistema de Gestão de Eventos Acadêmicos

O **SGEA** é um sistema web desenvolvido em **Django 5**, voltado para instituições acadêmicas que desejam organizar eventos, controlar inscrições e emitir certificados automaticamente.  
O projeto implementa fluxo completo com autenticação, perfis de usuário, CRUD de eventos e API REST com autenticação por token.

---

## 📦 Tecnologias utilizadas

- **Python 3.12+**
- **Django 5**
- **SQLite**
- **Django Rest Framework**
- **HTML + CSS (Design customizado)**
- **SMTP Gmail para envio de e-mails**
- **Pillow (para upload de imagens)**

---

## 🚀 Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-repo/sgea.git
cd sgea
2️⃣ Criar ambiente virtual
bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
3️⃣ Instalar dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Aplicar migrações
bash
Copiar código
python manage.py migrate
5️⃣ Criar superusuário (opcional)
bash
Copiar código
python manage.py createsuperuser
6️⃣ Executar servidor
bash
Copiar código
python manage.py runserver
Acesse:
👉 http://127.0.0.1:8000/

🔐 Perfis de Usuário
O sistema possui dois perfis principais:

Perfil	Permissões
Aluno	Visualiza eventos, inscreve, cancela inscrição
Organizador	Cria eventos, exclui eventos, administra inscrições

O perfil é configurado no cadastro do usuário.

📑 Funcionalidades Principais
✔ Cadastro e Login
Criar conta com nome, e-mail, senha e perfil.

Login seguro com autenticação nativa do Django.

✔ Listagem de Eventos
Exibe:

Nome, tipo, local, horário

Vagas totais

Inscritos

Status da inscrição do usuário

Banner do evento (se enviado)

✔ Inscrição em Evento
Quando o aluno se inscreve:

Sistema valida vagas

Evita inscrição duplicada

Registra no banco

Envia certificado por e-mail (versão simples)

✔ Cancelamento de Inscrição
Botão exclusivo para usuários inscritos.

✔ Criar Evento (Organizadores)
Campos:

Nome

Tipo

Datas

Horário

Local

Vagas

Banner

Validações:

Data inicial não pode ser no passado

Data final deve ser após a inicial

Vagas devem ser > 0

✔ Excluir Evento (Organizadores)
Um botão "Excluir" aparece apenas para quem é organizador daquele evento.

🧱 Estrutura do Projeto
arduino
Copiar código
SGEA/
│── eventos/
│── inscricoes/
│── usuarios/
│── certificados/
│── SGEA/
│── static/
│     └── css/style.css
│── media/
│     └── banners/
│── templates/
│── manage.py
│── db.sqlite3
📬 Envio de E-mails (Certificados)
Configuração feita em settings.py:

python
Copiar código
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "seuemail@gmail.com"
EMAIL_HOST_PASSWORD = "senha_de_app"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
⚠ Importante: deve ser usada senha de app do Gmail.

🌐 API REST
O projeto implementa uma API com token authentication:

GET /api/eventos/
Lista eventos.

POST /api/eventos/inscrever/<id>/
Inscreve usuário autenticado.

POST /api/eventos/cancelar/<id>/
Cancela inscrição.

Autenticação
http
Copiar código
Authorization: Token seu_token_aqui
