# 🚀 Sarjan Secure File Sharing API

A **production-ready secure file sharing system** built using **FastAPI, PostgreSQL, and Docker**.

This project allows users to upload, share, and download files securely using **JWT authentication and encrypted links**.

---

# 🧠 How This Project Works (Easy Explanation)

1. User signup/login करता है (JWT token मिलता है)
2. User file upload करता है
3. System database में file store करता है
4. Share API से secure link generate होता है
5. Download link encrypted होता है (secure access)

---

# 🔐 Features

* ✅ JWT Authentication (Secure Login)
* ✅ File Upload & Download System
* ✅ Role-Based Access (Client / Ops)
* ✅ Secure Shareable Links
* ✅ PostgreSQL Database
* ✅ Dockerized Deployment
* ✅ Email Support (SMTP)

---

# 🛠️ Tech Stack

* ⚡ FastAPI (Backend)
* 🐘 PostgreSQL (Database)
* 🐳 Docker & Docker Compose
* 🔐 JWT (Authentication)
* 🔑 Fernet Encryption
* 📧 SMTP Mail

---

# 📁 Project Structure

```
app/
 ├── main.py        # Main API
 ├── models/       # Database models
 ├── schemas/      # Request/Response schemas
 ├── auth.py       # Authentication logic
 ├── utils.py      # JWT & encryption
 ├── config.py     # Environment config
 ├── db.py         # Database connection
 └── services/     # Business logic
```

---

# ⚙️ Step-by-Step Setup (From Scratch)

## 🔹 Step 1: Clone Project

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

## 🔹 Step 2: Create Virtual Environment (Optional)

```
python3 -m venv .venv
source .venv/bin/activate
```

---

## 🔹 Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 Step 4: Setup Environment Variables

Create `.env` file:

```
nano .env
```

Paste this:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/filedb
SECRET_KEY=supersecretkey123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENCRYPTION_KEY=your_fernet_key
```

---

## 🔹 Step 5: Run with Docker (Recommended)

```
docker-compose up --build
```

---

## 🔹 Step 6: Check Running Containers

```
docker ps
```

---

## 🔹 Step 7: Open API Docs

```
http://localhost:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | `/`                | Health Check    |
| POST   | `/client/signup`   | Register User   |
| POST   | `/client/login`    | Login User      |
| GET    | `/client/files`    | Get User Files  |
| POST   | `/upload`          | Upload File     |
| GET    | `/share/{file_id}` | Generate Link   |
| GET    | `/download`        | Download File   |
| GET    | `/secure`          | Protected Route |

---

# 🧪 Example Commands (Testing API)

### 🔹 Signup

```
curl -X POST http://localhost:8000/client/signup \
-H "Content-Type: application/json" \
-d '{"email":"test@gmail.com","password":"123456"}'
```

---

### 🔹 Login

```
curl -X POST http://localhost:8000/client/login \
-H "Content-Type: application/json" \
-d '{"email":"test@gmail.com","password":"123456"}'
```

---

### 🔹 Upload File

```
curl -X POST http://localhost:8000/upload \
-F "file=@test.pdf"
```

---

# 🚀 Future Improvements

* 🔹 File Expiry System
* 🔹 Rate Limiting
* 🔹 Frontend UI (React)
* 🔹 AWS S3 Integration
* 🔹 CI/CD Pipeline (GitHub Actions)

---

# 👨‍💻 Author

**Sarjan Pratap**

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!
