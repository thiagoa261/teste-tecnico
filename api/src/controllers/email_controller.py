from fastapi import APIRouter, Header, Body, HTTPException, status, Depends
from src.core.guard import validate_session
from src.services import email_service
from pydantic import BaseModel

router = APIRouter()
class EmailRequest(BaseModel):
    content: str

@router.post("/processar")
async def classify_email(content: EmailRequest = Body(...), username: str = Depends(validate_session)):
    return await email_service.process_email(content.content)
