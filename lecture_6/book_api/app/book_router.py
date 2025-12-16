from fastapi import APIRouter, HTTPException, Query, Path, status
from sqlalchemy.orm import Session
from typing import List, Annotated
from .models import Book
from .schemas import BookResponse, BookUpdate, BookCreate
from .dependencies import SessionDep

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


#  Add a Book (CREATE)
@router.post("/books", response_model=BookResponse, status_code = status.HTTP_201_CREATED)
async def add_book(book: BookCreate, db: Session = SessionDep):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


#  Get All Books (READ)
@router.get("/books", response_model=List[BookResponse])
async def get_books(db: Session = SessionDep):
    return db.query(Book).all()


#  Get Book by ID (READ)
@router.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int = Annotated[int, Path(ge=1, lt=1_000_000)], db: Session = SessionDep):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


#  Update Book (PUT)
@router.put("/books/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, updated_book: BookUpdate, db: Session = SessionDep):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if updated_book.title is not None:
        book.title = updated_book.title
    if updated_book.author is not None:
        book.author = updated_book.author
    if updated_book.year is not None:
        book.year = updated_book.year

    db.commit()
    db.refresh(book)

    return book


#  Delete Book (DELETE)
@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = SessionDep):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}


#  Search Books (TITLE / AUTHOR / YEAR)
@router.get("/book/search", response_model=List[BookResponse])
async def search_books(
        title: str | None = Query(default=None),
        author: str | None = Query(default=None),
        year: int | None = Query(default=None),
        db: Session = SessionDep
):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    if year:
        query = query.filter(Book.year == year)

    results = query.all()

    if not results:
        search_params = []
        if title:
            search_params.append(f"title='{title}'")
        if author:
            search_params.append(f"author='{author}'")
        if year:
            search_params.append(f"year={year}")

        param_str = ", ".join(search_params) or "no parameters"
        raise HTTPException(
            status_code=404,
            detail=f"No books found matching: {param_str}"
        )

    return results

@router.get("/healthcheck", status_code= status.HTTP_200_OK)
async  def healthcheck():
    return {"status": "ok"}