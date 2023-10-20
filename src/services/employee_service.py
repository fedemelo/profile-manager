from sqlalchemy.orm import Session
from src.models.employee import Employee as EmployeeModel
from src.schemas.employee import EmployeeCreate, EmployeeResponse
from typing import List


def get_employee(db: Session, username: str):
    return (
        db.query(EmployeeModel)
        .filter(EmployeeModel.username == username)
        .first()
    )


def get_employees(db: Session):
    return db.query(EmployeeModel).all()


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = EmployeeModel(
        username=employee.username,
        name=employee.name,
        company_position=employee.company_position,
        avatar=employee.avatar,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_employees(db: Session, employees: List[EmployeeCreate]):
    return list(map(lambda employee: create_employee(db, employee), employees))


def update_employee(db: Session, username: str, employee: EmployeeCreate):
    db_employee = db.query(EmployeeModel).filter(
        EmployeeModel.username == username).first()
    db_employee.username = employee.username
    db_employee.name = employee.name
    db_employee.company_position = employee.company_position
    db_employee.avatar = employee.avatar
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, username: str):
    db_employee = get_employee(db, username)
    db.delete(db_employee)
    db.commit()
