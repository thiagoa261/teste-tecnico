from fastapi import APIRouter, Header, Body, HTTPException, status, Depends
from src.core.guard import validate_session
from src.services.email_service import process_email
from pydantic import BaseModel

router = APIRouter()

class EmailRequest(BaseModel):
    content: str

@router.post("/processar")
async def classify_email(content: EmailRequest = Body(...), username: str = Depends(validate_session)):
    return {"message": "Email recebido com sucesso"}
