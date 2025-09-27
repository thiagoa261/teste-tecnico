from pydantic import BaseModel
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., unique=True, index=True)
    password: str
