from fastapi import APIRouter, Body, Header, Depends
from src.models.user_model import User
from src.core.guard import validate_session
from src.services import auth_service

router = APIRouter()

@router.post("/login")
async def login(user: User = Body(...)):
    return await auth_service.login(user)

@router.post("/logout")
async def logout(token: str = Header(...), username: str = Depends(validate_session)):
    return await auth_service.logout(token)
