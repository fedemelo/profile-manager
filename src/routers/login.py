from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.login import LoginCreate, LoginResponse
from src.services import login as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/logins",
    tags=["logins"],
    responses={404: {"detail": "Not found"}},
)

@router.post("/", response_model=LoginResponse, status_code=201)
def create_login(login: LoginCreate, db: Session = Depends(get_db)):
    db_login = service.get_login(db, login.username)
    if db_login:
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_login(db=db, login=login)