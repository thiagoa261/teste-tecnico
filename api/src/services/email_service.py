import httpx
from src.core.config import settings
from src.db.mongo import db
from src.models.email_model import Email
from openai import OpenAI
import json
from fastapi import HTTPException, status

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
