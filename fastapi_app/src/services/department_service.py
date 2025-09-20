from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..implements import department_impl


router = APIRouter(prefix="/departments", tags=["departments"])

# your logic here
