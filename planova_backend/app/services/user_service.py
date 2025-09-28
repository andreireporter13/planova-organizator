#
#
#
from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, username: str, hashed_password: str, email: str):
    new_user = User(
        username=username,
        hashed_password=hashed_password,
        email=email,
        is_active=False  # By default inactive, needs email confirmation
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
