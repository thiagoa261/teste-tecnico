from fastapi import HTTPException, status, Header
from src.core import security

def validate_session(token: str = Header(...)) -> str:
    try:
        username = security.get_session_username(token)
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Sessão inválida ou expirada!"
            )
        
        return username
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao validar sessão: {str(e)}"
        )