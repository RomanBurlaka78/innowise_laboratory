from fastapi import FastAPI
import uvicorn
import models
from database import  engine
from lecture_5.book_api.src.book_router import router as book_router


# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")

# Connect router
app.include_router(router=book_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)