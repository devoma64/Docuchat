from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.auth import UserCreate, UserResponsePublic
from services.auth import register_user

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponsePublic)
def register(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    try:
        return register_user(
            db=db,
            email=user_data.email,
            password=user_data.password,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
