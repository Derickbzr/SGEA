from django.core.mail import EmailMessage
from .utils import gerar_certificado_pdf

def enviar_certificado(usuario, evento):
    pdf_buffer = gerar_certificado_pdf(usuario, evento)

    email = EmailMessage(
        subject="Seu certificado - SGEA",
        body=f"Olá {usuario.first_name}, segue seu certificado do evento {evento.nome}.",
        from_email="no-reply@sgea.com",
        to=[usuario.email],
    )

    email.attach(
        f"certificado_{evento.id}.pdf",
        pdf_buffer.read(),
        "application/pdf"
    )

    email.send()
