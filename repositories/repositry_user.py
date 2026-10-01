from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.model_user import User


def find_by_id(db: Session, user_id: str) -> User | None:
    return db.get(User, user_id)


def find_user_by_email(db: Session, email: str) -> User | None:
    result = db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


def create_user(db: Session, email: str, hashed_password: str) -> User:
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_by_id(db: Session, user_id: str, **field) -> User | None:
    user = db.get(User, user_id)

    if not user:
        return None

    for key, value in field.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)

    return user


def soft_delete(db: Session, user_id: str) -> User | None:
    return update_by_id(db, user_id, deleted_at=datetime.now(timezone.utc))
