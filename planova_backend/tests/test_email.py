import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_confirmation_email(to_email: str, confirm_url: str):
    SMTP_HOST = "81.180.202.99"
    SMTP_PORT = 25

    msg = MIMEMultipart()
    msg['From'] = "contact@return1101.ro"
    msg['To'] = to_email
    msg['Subject'] = "Confirm your email"

    body = f"Click on the link to confirm your email:\n\n{confirm_url}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.sendmail(msg['From'], [to_email], msg.as_string())
        print(f"Confirmation email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Test
send_confirmation_email("andrei.reporter13@gmail.com", "http://example.com/confirm?token=abc123")
