from fastapi import FastAPI
import uvicorn
from .models import Base
from .database import  engine
from .book_router import router as book_router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")

# Connect router
app.include_router(router=book_router)