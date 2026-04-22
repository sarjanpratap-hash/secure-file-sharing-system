from pydantic import BaseModel

class FileResponse(BaseModel):
    id: int
    filename: str
    uploader_id: int

    class Config:
        from_attributes = True
