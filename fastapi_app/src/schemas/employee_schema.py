from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True
