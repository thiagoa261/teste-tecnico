from fastapi import APIRouter, Header, Body, Depends, UploadFile, File
from src.core.guard import validate_session
from src.services import email_service
from pydantic import BaseModel

router = APIRouter()
class EmailProcessRequest(BaseModel):
    content: str
class SaveEmailRequest(BaseModel):
    content: str
    category: str
    response: str
    justification: str

class ListEmailsRequest(BaseModel):
    offset: int
    limit: int

@router.post("/processar")
async def classify_email(content: EmailProcessRequest = Body(...), username: str = Depends(validate_session)):
    return await email_service.process_email(content.content)

@router.post("/processar/file")
async def classify_email_file(file: UploadFile = File(...), username: str = Depends(validate_session)):
    content = await file.read()

    try:
        text = content.decode("utf-8")  
    except UnicodeDecodeError:
        from PyPDF2 import PdfReader
        import io
        pdf_reader = PdfReader(io.BytesIO(content))
        text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])

    return await email_service.process_email(text)

@router.post("/salvar")
async def save_email(email: SaveEmailRequest = Body(...), username: str = Depends(validate_session)):
    return await email_service.save_email(email.dict())

@router.post("/listar")
async def list_emails(params: ListEmailsRequest = Body(...), username: str = Depends(validate_session)):
    return await email_service.list_emails(params.offset, params.limit)