from sqlalchemy.orm import Session
from src.models.skill import Skill as SkillModel
from src.schemas.skill import SkillCreate, Skill
from typing import List


def get_skill(db: Session, name: str):
    return (
        db.query(SkillModel)
        .filter(SkillModel.name == name)
        .first()
    )


def get_skills(db: Session):
    return db.query(SkillModel).all()


def create_skill(db: Session, skill: SkillCreate):
    db_skill = SkillModel(
        name=skill.name,
        description=skill.description,
        level=skill.level,
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def create_skills(db: Session, skills: List[SkillCreate]):
    skills.map(lambda skill: create_skill(db, skill))


def update_skill(db: Session, name: str, skill: SkillCreate):
    db_skill = get_skill(db, name)
    db_skill.name = skill.name
    db_skill.description = skill.description
    db_skill.level = skill.level
    db.commit()
    db.refresh(db_skill)
    return db_skill


def delete_skill(db: Session, name: str):
    db_skill = get_skill(db, name)
    db.delete(db_skill)
    db.commit()
    return db_skill
