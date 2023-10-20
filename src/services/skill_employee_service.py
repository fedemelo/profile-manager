from sqlalchemy.orm import Session
from src.models.employee import Employee as EmployeeModel
from src.schemas.employee import EmployeeResponse
from src.models.skill import Skill as SkillModel
from typing import List
from uuid import uuid4


def create_full_employee(db: Session, employee: EmployeeResponse):
    db_employee = EmployeeModel(
        username=employee.username,
        name=employee.name,
        company_position=employee.company_position,
        avatar=employee.avatar,
    )
    for skill in employee.skills:
        db_skill = SkillModel(
            id=str(uuid4()),
            name=skill.name,
            description=skill.description,
            level=skill.level,
            employee_username=employee.username,
        )
        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_full_employees(db: Session, employees: List[EmployeeResponse]):
    return list(map(lambda employee: create_full_employee(db, employee), employees))
