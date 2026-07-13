import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_mail(destinatario: str, asunto: str, cuerpo: str) -> bool:
    """Envía un mail al destinatario con el reporte generado."""
    try:
        remitente = os.getenv("GMAIL_USER")
        password = os.getenv("GMAIL_APP_PASSWORD")

        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = asunto
        mensaje["From"] = remitente
        mensaje["To"] = destinatario

        parte = MIMEText(cuerpo, "plain", "utf-8")
        mensaje.attach(parte)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remitente, password)
            servidor.sendmail(remitente, destinatario, mensaje.as_string())

        print(f"✅ Mail enviado a {destinatario}")
        return True

    except Exception as e:
        print(f"❌ Error al enviar mail a {destinatario}: {e}")
        return False