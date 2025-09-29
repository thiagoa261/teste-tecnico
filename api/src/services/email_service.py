import httpx
from src.core.config import settings
from src.db.mongo import db
from src.models.email_model import Email
from openai import OpenAI
import json
from fastapi import HTTPException, status
from datetime import datetime

async def process_email(content: str):
    try:
        client = OpenAI(api_key=settings.gpt_api_token)

        response = client.chat.completions.create(
            model=settings.gpt_model,
            messages=[
                { "role": "system", "content": settings.gpt_prompt },
                { "role": "user", "content": "Email: " + content }
            ]
        )
        response = response.choices[0].message.content

        try:
            parsed = json.loads(response)
            parsed["content"] = content
            return parsed
        
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Resposta do modelo não está em formato JSON válido"
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao processar email: {str(e)}"
        )

async def save_email(data: dict):
    try:
        email = Email(
            content=data["content"],
            category=data["category"],
            response=data["response"],
            justification=data["justification"],
            created_at=datetime.utcnow()
        )

        result = await db.emails.insert_one(email.dict())
        
        return {
            "message": "Email salvo com sucesso!",
            "_id": str(result.inserted_id),
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao salvar email: {str(e)}"
        )

async def list_emails(offset: int, limit: int):
    try:
        cursor = db.emails.find().skip(offset).limit(limit)
        emails = await cursor.to_list(length=limit)
        total = await db.emails.count_documents({})

        # transforma o ObjectId em string
        for email in emails:
            email["_id"] = str(email["_id"])

        return {
            "total": total,
            "offset": offset,
            "limit": limit,
            "emails": emails
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar emails: {str(e)}"
        )