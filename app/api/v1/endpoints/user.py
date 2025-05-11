from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.crud import user as crud_user
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserResponse)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user_in)

@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)
