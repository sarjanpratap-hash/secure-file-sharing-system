from fastapi_mail import FastMail, MessageSchema
from app.email import conf

async def send_verification_email(email: str, token: str):
    link = f"http://127.0.0.1:8000/client/email-verify/{token}"

    message = MessageSchema(
        subject="Verify your email",
        recipients=[email],
        body=f"Click this link to verify your email:\n{link}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
