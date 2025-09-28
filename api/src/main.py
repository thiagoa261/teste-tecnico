from fastapi import FastAPI
from src.controllers import email_controller, auth_controller
from src.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from src.db.mongo import db
from src.core import security

api = FastAPI(title="API para classificação de e-mails")

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
api.include_router(auth_controller.router, prefix="/auth", tags=["Auth"])
api.include_router(email_controller.router, prefix="/email", tags=["Emails"])

@api.on_event("startup")
async def startup_event():
    admin = await db.users.find_one({"username": settings.admin_username})
    if not admin:
        await db.users.insert_one({
            "username": settings.admin_username,
            "password": security.hash_password(settings.admin_password)
        })
        print(f"✅ Usuário admin criado: {settings.admin_username}")
    else:
        print(f"ℹ️ Usuário admin já existe: {settings.admin_username}")
