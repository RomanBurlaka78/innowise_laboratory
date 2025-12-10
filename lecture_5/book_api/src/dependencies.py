from fastapi import Depends
from lecture_5.book_api.src.database import SessionLocal


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Depends(get_db)