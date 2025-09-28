import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv(override=True)

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 25))  # port implicit SMTP local e 25
SMTP_USER = os.getenv("SMTP_USER", None)
SMTP_PASS = os.getenv("SMTP_PASS", None)


def send_confirmation_email(to_email: str, confirm_url: str):
    msg = MIMEMultipart()
    msg['From'] = "contact@return1101.ro"
    msg['To'] = to_email
    msg['Subject'] = "Confirm your email"

    body = f"Click on the link to confirm your email:\n\n{confirm_url}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            # Nu facem login dacă SMTP_USER sau SMTP_PASS nu există (SMTP local)
            if SMTP_USER and SMTP_PASS:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(msg['From'], to_email, msg.as_string())
        print(f"Confirmation email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
