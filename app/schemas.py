from pydantic import BaseModel, EmailStr, Field

# ================= USER =================

class UserSignup(BaseModel):
    email: EmailStr = Field(..., example="user@gmail.com")
    password: str = Field(..., example="strongpassword123")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="user@gmail.com")
    password: str = Field(..., example="strongpassword123")

# ================= FILE =================

class FileResponse(BaseModel):
    id: int = Field(..., example=1)
    filename: str = Field(..., example="resume.pdf")

    class Config:
        from_attributes = True

class Message(BaseModel):
    msg: str = Field(..., example="Success")
