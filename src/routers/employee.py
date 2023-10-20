from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.employee import Employee, EmployeeCreate
from src.services import employee_service as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/employees",
    tags=["employees"],
    responses={404: {"detail": "Not found"}},
)

@router.get("/", response_model=List[Employee])
def get_employees(db: Session = Depends(get_db)):
    return service.get_employees(db)

@router.get("/{employee_username}", response_model=Employee)
def get_employee(employee_username: str, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee.username)
    if db_employee:
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_employee(db=db, employee=employee)

@router.post("/many", response_model=List[Employee])
def create_employees(employees: List[EmployeeCreate], db: Session = Depends(get_db)):
    for employee in employees:
        db_employee = service.get_employee(db, employee.username)
        if db_employee:
            raise HTTPException(status_code=400, detail="Username already registered")

    return service.create_employees(db=db, employees=employees)

@router.put("/{employee_username}", response_model=Employee)
def update_employee(employee_username: str, employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.update_employee(db=db, employee_username=employee_username, employee=employee)

@router.delete("/{employee_username}", response_model=Employee)
def delete_employee(employee_username: str, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.delete_employee(db=db, employee_username=employee_username)
