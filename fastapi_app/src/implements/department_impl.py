from sqlalchemy.orm import Session
from ..models import department_model 
from ..schemas import department_schema 

def create_department(db: Session, dept: department_schema.DepartmentCreate):
    new_dept = department_model.Department(**dept.dict())
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept
