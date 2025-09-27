from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings

if settings.mongo_user and settings.mongo_pass:
    mongo_uri = f"mongodb://{settings.mongo_user}:{settings.mongo_pass}@{settings.mongo_host}:{settings.mongo_port}"
else:
    mongo_uri = f"mongodb://{settings.mongo_host}:{settings.mongo_port}"

try:
    client = AsyncIOMotorClient(mongo_uri)
    db = client[settings.mongo_db]

except Exception as e:
    print(f"❌ Falha ao inicializar cliente MongoDB: {e}")
    client = None
    db = None
