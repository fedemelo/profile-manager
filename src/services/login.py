from sqlalchemy.orm import Session
from src.models.login import Login as LoginModel
from src.schemas.login import LoginCreate


def get_login(db: Session, username: str):
    return (
        db.query(LoginModel)
        .filter(LoginModel.username == username)
        .first()
    )


def create_login(db: Session, login: LoginCreate):
    db_login = LoginModel(
        username=login.username,
        password=login.password,
    )
    db.add(db_login)
    db.commit()
    db.refresh(db_login)
    return db_login
