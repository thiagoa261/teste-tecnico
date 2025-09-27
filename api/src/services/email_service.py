import httpx
from src.core.config import settings
from src.db.mongo import db
from src.models.email_model import Email

async def process_email(content: str):
    # Chamada ao GPT para classificar
    headers = {"Authorization": f"Bearer {settings.gpt_api_token}"}
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": settings.gpt_prompt},
            {"role": "user", "content": content}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(settings.gpt_api_url, json=payload, headers=headers)
        result = response.json()
        classification = result["choices"][0]["message"]["content"]

    # Salvando no Mongo
    email_doc = Email(content=content, category="TODO", response=classification)
    await db.emails.insert_one(email_doc.dict())

    return email_doc
