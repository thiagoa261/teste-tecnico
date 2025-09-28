from fastapi import APIRouter, Body, Header, Depends, HTTPException, status
from src.models.user_model import User
from src.core.guard import validate_session
from src.services import auth_service

router = APIRouter()

@router.get("/me")
async def get_me(username: str = Depends(validate_session)):
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não autenticado")
    return { "username": username }

@router.post("/login")
async def login(user: User = Body(...)):
    return await auth_service.login(user)

@router.post("/logout")
async def logout(token: str = Header(...), username: str = Depends(validate_session)):
    return await auth_service.logout(token)