from pydantic import BaseModel, Field, field_validator
from typing import Optional

# Shared fields
class BookBase(BaseModel):
    title: str = Field(..., title = "Title", min_length=1)
    author: str = Field(..., title = "Author", min_length=1)
    year: Optional[int] = Field(None, ge=0)

    # --- Validators ---
    @field_validator("title", "author")
    def no_empty_or_spaces(cls, value):
        if not value or not value.strip():
            raise ValueError("Field cannot be empty or spaces only")
        return value.strip()

#  For POST
class BookCreate(BookBase):
    pass

# For PUT
class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = Field(None, ge=0)

    @field_validator("title", "author")
    def no_empty_or_spaces_update(cls, value):
        if value is None:
            return value
        if not value.strip():
            raise ValueError("Field cannot be empty or spaces only")
        return value.strip()

#  For GET
class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True