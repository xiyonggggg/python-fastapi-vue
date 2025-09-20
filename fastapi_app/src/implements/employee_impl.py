from sqlalchemy.orm import Session
from ..models import employee_model
from ..schemas import employee_schema


def create_employee(db: Session, emp: employee_schema.EmployeeCreate):
    new_emp = employee_model.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_employees(db: Session):
    return db.query(employee_model.Employee).all()
