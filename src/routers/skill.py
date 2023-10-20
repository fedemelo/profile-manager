from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.skill import SkillResponse, SkillCreate
from src.services import skill_service as service
from src.services import employee_service as employee_service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[SkillResponse], status_code=200)
def get_skills(db: Session = Depends(get_db)):
    return service.get_skills(db)


@router.get("/{skill_name}", response_model=SkillResponse, status_code=200)
def get_skill(skill_name: str, db: Session = Depends(get_db)):
    db_skill = service.get_skill(db, skill_name)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="SkillResponse not found")
    return db_skill


@router.post("/", response_model=SkillResponse, status_code=201)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = service.get_skill(db, skill.name)
    if db_skill:
        raise HTTPException(
            status_code=400, detail="SkillResponse already registered")
    return service.create_skill(db=db, skill=skill)


@router.post("/many", response_model=List[SkillResponse], status_code=201)
def create_skills(skills: List[SkillCreate], db: Session = Depends(get_db)):
    for skill in skills:
        db_skill = service.get_skill(db, skill.name)
        if db_skill:
            raise HTTPException(
                status_code=400, detail="SkillResponse already registered")

    return service.create_skills(db=db, skills=skills)


@router.put("/{skill_name}", response_model=SkillResponse, status_code=200)
def update_skill(skill_name: str, skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = service.get_skill(db, skill_name)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="SkillResponse not found")
    return service.update_skill(db=db, name=skill_name, skill=skill)


@router.delete("/{skill_name}", status_code=204)
def delete_skill(skill_name: str, db: Session = Depends(get_db)):
    db_skill = service.get_skill(db, skill_name)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="SkillResponse not found")
    return service.delete_skill(db=db, name=skill_name)


@router.get("/employee/{employee_username}", response_model=List[SkillResponse], status_code=200)
def get_employee_skills(employee_username: str, db: Session = Depends(get_db)):
    db_employee = employee_service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.get_employee_skills(db, employee_username)


@router.post("/employee/{employee_username}", response_model=SkillResponse, status_code=201)
def create_employee_skill(employee_username: str, skill: SkillCreate, db: Session = Depends(get_db)):
    db_employee = employee_service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.create_employee_skill(db=db, employee_username=employee_username, skill=skill)


@router.put("/employee/{employee_username}/{skill_name}", response_model=SkillResponse, status_code=200)
def update_employee_skill(employee_username: str, skill_name: str, skill: SkillCreate, db: Session = Depends(get_db)):
    db_employee = employee_service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.update_employee_skill(db=db, employee_username=employee_username, name=skill_name, skill=skill)
