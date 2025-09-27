from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    session_duration: int

    mongo_host: str
    mongo_port: int
    mongo_user: str | None = None
    mongo_pass: str | None = None
    mongo_db: str

    redis_host: str
    redis_port: int
    redis_password: str | None = None

    admin_username: str
    admin_password: str

    gpt_api_token: str
    gpt_model: str
    gpt_prompt: str

    class Config:
        env_file = ".env"

settings = Settings()
