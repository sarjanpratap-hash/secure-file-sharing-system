from app.auth.token import create_email_token, verify_email_token
from app.send_mail import send_verification_email
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.db import Base, engine
from dotenv import load_dotenv
load_dotenv()
from app.models.file import File as FileModel
from jose import jwt
from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal

import os

app = FastAPI(
    title="sarjan Secure File Sharing API 🚀",
    description="Secure file sharing system with authentication and email verification",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "storage"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"msg": "Working 🚀"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    new_file = FileModel(filename=file.filename, owner="abhi")
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {"msg": "File uploaded", "file_id": new_file.id}

@app.get("/share/{file_id}")
def generate_link(file_id: int):

    return {
        "download_url": f"http://127.0.0.1:8000/download?token={token}"
    }

# ================= CLIENT =================

@app.post("/client/signup")
async def signup():
    email = "sarjanpratap@gmail.com"   # अभी fix email

    token = create_email_token(email)
    await send_verification_email(email, token)

    return {"msg": "Verification email sent"}

@app.post("/client/login")
def login():
    token = create_token({"user": "client"})
    return {"access_token": token}

@app.get("/client/files")
def list_files():
    return ["file1.jpg", "file2.pdf"]

@app.get("/client/download/{file_id}")
def get_download(file_id: int):
    return {"link": f"/client/download-file/{file_id}"}

@app.get("/client/download-file/{enc}")
def download_file(enc: str):
    return {"msg": f"Downloading {enc}"}

@app.get("/client/email-verify/{token}")
def verify_email(token: str):
    try:
        email = verify_email_token(token)
        return {"msg": f"{email} verified successfully"}
    except:
        return {"msg": "Invalid or expired token"}

# ================= OPS =================

@app.post("/ops/upload")
def ops_upload():
    return {"msg": "File uploaded by ops"}


# ================= AUTH =================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/client/login")

@app.get("/secure")
def secure(token: str = Depends(oauth2_scheme)):
    return {"msg": "secured"}
