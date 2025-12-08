from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io
from django.core.mail import EmailMessage
from io import BytesIO

def gerar_certificado_pdf(nome_usuario, nome_evento):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 22)
    p.drawString(100, 750, "CERTIFICADO DE PARTICIPAÇÃO")

    p.setFont("Helvetica", 16)
    p.drawString(100, 700, f"Certificamos que {nome_usuario}")
    p.drawString(100, 670, f"participou do evento: {nome_evento}")

    p.setFont("Helvetica-Oblique", 12)
    p.drawString(100, 630, "SGEA - Sistema de Gestão de Eventos Acadêmicos")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


def enviar_certificado(usuario, evento):
    nome_usuario = usuario.first_name or usuario.username
    nome_evento = evento.nome

    pdf_buffer = gerar_certificado_pdf(nome_usuario, nome_evento)

    email = EmailMessage(
        subject="Certificado de Participação - SGEA",
        body=f"Olá {nome_usuario}, segue seu certificado do evento '{nome_evento}'.",
        from_email="no-reply@sgea.com",
        to=[usuario.email],
    )

    email.attach(
        f"certificado_{evento.id}.pdf",
        pdf_buffer.read(),
        "application/pdf"
    )

    email.send()
