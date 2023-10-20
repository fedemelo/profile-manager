from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from src.schemas.employee import EmployeeResponse, EmployeeCreate
import src.services.employee_service as service
import src.services.skill_employee_service as skill_employee_service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/employees",
    tags=["employees"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[EmployeeResponse], status_code=200)
def get_employees(db: Session = Depends(get_db)):
    return service.get_employees(db)


@router.get("/{employee_username}", response_model=EmployeeResponse, status_code=200)
def get_employee(employee_username: str, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(
            status_code=404, detail="EmployeeResponse not found")
    return db_employee


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee.username)
    if db_employee:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return service.create_employee(db=db, employee=employee)


@router.post("/many", response_model=List[EmployeeResponse], status_code=201)
def create_employees(employees: List[EmployeeCreate], db: Session = Depends(get_db)):
    for employee in employees:
        db_employee = service.get_employee(db, employee.username)
        if db_employee:
            raise HTTPException(
                status_code=400, detail="Username already registered")
    return service.create_employees(db=db, employees=employees)


@router.post("/full", response_model=EmployeeResponse, status_code=201)
def create_full_employee(employee: EmployeeResponse, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee.username)
    if db_employee:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return skill_employee_service.create_full_employee(db=db, employee=employee)


@router.post("/full/many", response_model=List[EmployeeResponse], status_code=201)
def create_full_employees(employees: List[EmployeeResponse], db: Session = Depends(get_db)):
    for employee in employees:
        db_employee = service.get_employee(db, employee.username)
        if db_employee:
            raise HTTPException(
                status_code=400, detail="Username already registered")
    return skill_employee_service.create_full_employees(db=db, employees=employees)


@router.put("/{employee_username}", response_model=EmployeeResponse, status_code=200)
def update_employee(employee_username: str, employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(
            status_code=404, detail="EmployeeResponse not found")
    return service.update_employee(db=db, username=employee_username, employee=employee)


@router.delete("/{employee_username}", status_code=204)
def delete_employee(employee_username: str, db: Session = Depends(get_db)):
    db_employee = service.get_employee(db, employee_username)
    if db_employee is None:
        raise HTTPException(
            status_code=404, detail="EmployeeResponse not found")
    return service.delete_employee(db=db, username=employee_username)