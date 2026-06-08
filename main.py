from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This is the "add_middleware" code section that grants your Vite page permission to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordSubmission(BaseModel):
    password: str

@app.post("/api/hash-password")
def hash_password(data: PasswordSubmission):
    plain_password = data.password
    hashed_password = pwd_context.hash(plain_password)
    return {
        "status": "success",
        "original_length": len(plain_password),
        "secure_hash": hashed_password
    }