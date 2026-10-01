from sqlalchemy.orm import Session

from repositories.user import create_user, find_user_by_email


def register_user(db: Session, email: str, password: str):
    existing_user = find_user_by_email(db, email)

    if existing_user:
        raise ValueError("User already exists.")

    hashed_password = password

    return create_user(
        db=db,
        email=email,
        hashed_password=hashed_password,
    )
