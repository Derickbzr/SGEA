# 🎓 **SGEA – Sistema de Gestão de Eventos Acadêmicos**

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-success.svg)
![License](https://img.shields.io/badge/license-Educational-lightgrey.svg)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow.svg)

---

## 🧠 **Descrição do Projeto**

O **SGEA (Sistema de Gestão de Eventos Acadêmicos)** é uma aplicação web desenvolvida em **Python + Django** para o gerenciamento de **eventos acadêmicos** como palestras, seminários, minicursos e semanas universitárias.

O sistema foi criado com foco em **boas práticas de desenvolvimento (MVC, segurança, modularidade)** e permite que alunos, professores e organizadores **interajam em um ambiente unificado**.

---

## 🚀 **Funcionalidades**

✅ **Usuários (Autenticação e Perfis)**
- Cadastro e login de usuários.  
- Perfis distintos: **Aluno**, **Professor** e **Organizador**.  
- Validação de campos obrigatórios (nome, telefone, instituição, login e senha).

🎟️ **Eventos**
- Criação, listagem e inscrição em eventos.  
- Somente organizadores podem criar novos eventos.  
- Exibição de eventos com layout institucional (tema azul e branco).

🧾 **Certificados**
- Emissão e listagem de certificados vinculados a usuários inscritos.  
- Somente organizadores podem emitir certificados.  
- Tabelas responsivas e visual limpo.

🔐 **Autenticação**
- Login seguro e senhas com hash.
- Controle de permissões por perfil.
- Logout e redirecionamento seguro.

---

## 🏗️ **Estrutura do Projeto**

```
SGEA/
│
├── manage.py
├── db.sqlite3
│
├── SGEA/                   # Configurações principais (settings, urls, wsgi)
│
├── usuarios/               # App de autenticação e perfis
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/usuarios/
│       ├── login.html
│       └── cadastro.html
│
├── eventos/                # App de gerenciamento de eventos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/eventos/
│       ├── listar.html
│       └── novo.html
│
├── certificados/           # App de certificados
│   ├── views.py
│   ├── urls.py
│   └── templates/certificados/
│       ├── listar.html
│       └── emitir.html
│
├── templates/              # Templates globais
│   ├── base.html
│   └── home.html
│
└── static/                 # Arquivos estáticos (CSS)
    └── css/
        └── style.css
```

---

## 🛠️ **Tecnologias Utilizadas**

| Tecnologia | Descrição |
|-------------|------------|
| **Python 3.13** | Linguagem principal |
| **Django 5.2** | Framework web MVC |
| **SQLite3** | Banco de dados padrão |
| **HTML5 / CSS3** | Estrutura e estilização |
| **Bootstrap-like CSS** | Tema customizado (branco e azul institucional) |

---

## ⚙️ **Instalação e Execução**

### 🔹 Clonar o repositório
```bash
git clone https://github.com/seu-usuario/SGEA.git
cd SGEA
```

### 🔹 Criar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 🔹 Instalar as dependências
```bash
pip install django
```

### 🔹 Aplicar migrações
```bash
python manage.py migrate
```

### 🔹 Criar superusuário
```bash
python manage.py createsuperuser
```

### 🔹 Executar o servidor
```bash
python manage.py runserver
```

Acesse:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👨‍🏫 **Perfis de Usuário**

| Perfil | Permissões |
|--------|-------------|
| 🧑‍🎓 **Aluno** | Pode se inscrever em eventos e visualizar certificados. |
| 👩‍🏫 **Professor** | Pode se inscrever e visualizar eventos. |
| 🧑‍💼 **Organizador** | Pode criar eventos e emitir certificados. |

---

## 💡 **Principais Rotas**

| URL | Descrição |
|-----|------------|
| `/` | Página inicial |
| `/usuarios/login/` | Login |
| `/usuarios/cadastro/` | Cadastro |
| `/eventos/` | Listar eventos |
| `/eventos/novo/` | Criar novo evento |
| `/certificados/` | Listar certificados |
| `/certificados/emitir/` | Emitir novo certificado |

---

## 📘 **Boas Práticas e Arquitetura**

- Estrutura modular em múltiplos apps Django.  
- Uso do modelo de usuário customizado (`AbstractUser`).  
- Senhas criptografadas.  
- Templates e estáticos organizados.  
- Layout responsivo com CSS customizado.  

---

## 📈 **Próximas Melhorias**

- Geração de certificados em PDF.  
- Envio de certificados por e-mail.  
- Filtro de certificados por usuário autenticado.  
- Dashboard de estatísticas para organizadores.

---

## 👨‍💻 **Autor**

**Derick Bezerra**  
📍 Projeto desenvolvido para disciplina de **Desenvolvimento Web com Django**  
📅 Faculdade — 2025  
💬 Contato: *[derick.bezerra@sempreceub.com]*  

---

## 🧩 **Licença**

Este projeto é de uso **educacional** e pode ser utilizado para fins acadêmicos.  
Sinta-se à vontade para modificar e expandir.

---

> 💡 *“A tecnologia só faz sentido quando ajuda a conectar conhecimento e pessoas.”*
