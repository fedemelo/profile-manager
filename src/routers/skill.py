from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.skill import Skill, SkillCreate
from src.services import skill_service as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"detail": "Not found"}},
)

@router.get("/", response_model=List[Skill])
def get_skills(db: Session = Depends(get_db)):
    return service.get_skills(db)

