from fastapi import HTTPException, status
from src.models.user_model import User
from src.core import security
from src.db.mongo import db

async def login(user: User):
    user_doc = await db.users.find_one({"username": user.username})

    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválida"
        )

    if not security.verify_password(user.password, user_doc["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválida"
        )

    token = security.generate_session_token()
    security.save_session(token, user.username)

    return { "session_token": token }

async def logout(token: str):
    try:
        deleted = security.delete_session(token)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Sessão não encontrada ou já encerrada"
            )
        
        return { "message": "Sessão encerrada com sucesso" }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao encerrar sessão: {str(e)}"
        )

async def create_user(user: User):
    try:
        existing = await db.users.find_one({"username": user.username})
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuário já existe"
            )

        await db.users.insert_one({
            "username": user.username,
            "password": security.hash_password(user.password)
        })

        return { "message": f"Usuário {user.username} criado com sucesso" }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar usuário: {str(e)}"
        )
