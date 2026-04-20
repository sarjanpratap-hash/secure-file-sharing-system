from itsdangerous import URLSafeTimedSerializer
import os

SECRET_KEY = "supersecretkey123"

serializer = URLSafeTimedSerializer(SECRET_KEY)

def create_email_token(email: str):
    return serializer.dumps(email, salt="email-confirm")

def verify_email_token(token: str):
    return serializer.loads(token, salt="email-confirm", max_age=3600)
