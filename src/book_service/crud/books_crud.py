from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from book_service import schemas
from db import models


# Create
async def create_book(db: AsyncSession, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


# Read
async def get_book(db: AsyncSession, book_id: int):
    book = await db.execute(
        select(models.Book).where(models.Book.id == book_id)
    )
    return book.scalar_one_or_none()


# Update
async def update_book(
        db: AsyncSession,
        book_id: int, book_update: schemas.BookCreate):
    db_book = await get_book(db, book_id)
    if db_book:
        for field, value in book_update.dict().items():
            setattr(db_book, field, value)
        await db.commit()
        await db.refresh(db_book)
    return db_book


# Delete
async def delete_book(
        db: AsyncSession,
        book_id: int):
    db_book = await get_book(db, book_id)
    if db_book:
        await db.delete(db_book)
        await db.commit()
    return db_book
