def create_download_token(file_id: int):
    from datetime import datetime, timedelta
    from jose import jwt

    data = {"file_id": file_id}
    expire = datetime.utcnow() + timedelta(minutes=10)  # 10 min expiry
    data.update({"exp": expire})

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
