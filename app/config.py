from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

    if ENCRYPTION_KEY:
        ENCRYPTION_KEY = ENCRYPTION_KEY.encode()
    else:
        raise ValueError("ENCRYPTION_KEY missing")

settings = Settings()
