from fastapi import FastAPI
from .healthcheck_router import router as healthcheck_router
from .models import Base
from .database import  engine
from .book_router import router as book_router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")

# Connect router
app.include_router(router=book_router)
app.include_router(router=healthcheck_router)