import redis
from src.core.config import settings

try:
    redis_client = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
        decode_responses=True
    )

    redis_client.ping()
    print("✅ Conectado ao Redis com sucesso!")

except Exception as e:
    print(f"❌ Erro inesperado ao conectar ao Redis: {e}")
    redis_client = None
