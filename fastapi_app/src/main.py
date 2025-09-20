from fastapi import FastAPI
from .database.db import Base, engine
from .services import employee_service, department_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee CRUD API")

app.include_router(employee_service.router)
