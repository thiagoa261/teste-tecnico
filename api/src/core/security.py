import hashlib
import uuid
from src.db.redis import redis_client

SESSION_EXPIRE_SECONDS = 3600  # 1 hora

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def generate_session_token() -> str:
    return hashlib.sha256(str(uuid.uuid4()).encode("utf-8")).hexdigest()

def save_session(token: str, username: str):
    redis_client.set(token, username, ex=SESSION_EXPIRE_SECONDS)

def get_session_username(token: str) -> str | None:
    return redis_client.get(token)

def delete_session(token: str):
    return redis_client.delete(token)
