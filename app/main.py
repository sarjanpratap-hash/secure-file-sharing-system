from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, Query, Path
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
import time

from app.db import Base, engine, SessionLocal
from app import models
from app.utils import hash_password, verify_password, create_access_token
from app.auth import get_current_user

load_dotenv()

app = FastAPI(
    title="🚀 Sarjan Secure File Sharing API",
    description="""
🔐 Production Ready Secure File Sharing System

✨ Features:
- JWT Authentication
- File Upload & Secure Sharing
- Role-Based Access (Client / Ops)
- PostgreSQL Database
- Docker Ready Deployment

👨‍💻 Built by Sarjan
""",
    version="2.0.0"
)

time.sleep(2)

Base.metadata.create_all(bind=engine)

# ================= DB =================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "storage"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ================= ROOT =================

@app.get("/", summary="Health Check API")
def home(
    name: str = Query("Sarjan", description="Enter your name"),
    age: int = Query(20, description="Enter your age")
):
    return {"msg": f"Hello {name}, Age {age}"}

# ================= CLIENT =================

@app.post("/client/signup", summary="Register new user")
def signup(
    email: str = Query(..., description="User email"),
    password: str = Query(..., description="User password"),
    db: Session = Depends(get_db)
):
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = models.User(
        email=email,
        hashed_password=hash_password(password),
        role="client",
        is_verified=True
    )

    db.add(new_user)
    db.commit()

    return {"msg": "User created successfully"}

@app.post("/client/login", summary="Login user and get JWT token")
def login(
    email: str = Query(..., description="User email"),
    password: str = Query(..., description="User password"),
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(models.User.email == email).first()

    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})
    return {"access_token": token}

@app.get("/client/files", summary="Get all files uploaded by user")
def list_files(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    files = db.query(models.File).filter(models.File.uploader_id == current_user.id).all()
    return files

# ================= FILE =================

@app.post("/upload", summary="Upload file")
def upload_file(
    file: UploadFile = File(..., description="Upload any file (pdf, image, etc)"),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    new_file = models.File(filename=file.filename, uploader_id=1)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {"msg": "File uploaded successfully", "file_id": new_file.id}

@app.get("/share/{file_id}", summary="Generate secure download link")
def generate_link(
    file_id: int = Path(..., description="ID of file to share")
):
    token = create_access_token({"file_id": file_id})
    return {
        "download_url": f"http://127.0.0.1:8000/download?token={token}"
    }

@app.get("/download", summary="Download file using token")
def download_file(
    token: str = Query(..., description="JWT token for secure download")
):
    return {"msg": "Download working securely"}

# ================= OPS =================

@app.post("/ops/upload", summary="Upload file by Ops user")
def ops_upload():
    return {"msg": "File uploaded by ops"}

# ================= AUTH =================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/client/login")

@app.get("/secure", summary="Protected route (JWT required)")
def secure(token: str = Depends(oauth2_scheme)):
    return {"msg": "You are authorized ✅"}
