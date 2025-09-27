from pydantic import BaseModel
from datetime import datetime

class Email(BaseModel):
    content: str
    category: str
    response: str
    created_at: datetime = datetime.utcnow()
