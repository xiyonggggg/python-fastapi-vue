from fastapi import APIRouter, Depends
from ..implements import employee_impl
from ..schemas import employee_schema
from sqlalchemy.orm import Session
from ..database import db


router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=list[employee_schema.Employee])
def list_employees(db_session: Session = Depends(db.get_db)):
    return employee_impl.get_employees(db_session)


@router.post("/", response_model=employee_schema.Employee)
def add_employee(employee: employee_schema.EmployeeCreate, db_session: Session = Depends(db.get_db)):
    return employee_impl.create_employee(db_session, employee)
