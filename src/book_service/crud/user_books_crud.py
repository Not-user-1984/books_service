from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from book_service import schemas

from db import models


async def create_user_book(
    db: AsyncSession, user_book: schemas.UserBookCreate
):
    db_user_book = models.UserBook(**user_book.dict())
    db.add(db_user_book)
    await db.commit()
    await db.refresh(db_user_book)
    return db_user_book


async def get_user_book(db: AsyncSession, user_book_id: int):
    user_book = await db.execute(
        select(models.UserBook).where(models.UserBook.id == user_book_id)
    )
    return user_book.scalar_one_or_none()


async def get_user_books(db: AsyncSession, user_id: int):
    user_books = await db.execute(
        select(models.UserBook).where(models.UserBook.user_id == user_id)
    )
    return user_books.scalars().all()


async def update_user_book(
    db: AsyncSession,
    user_book_id: int,
    user_book_update: schemas.UserBookCreate,
):
    db_user_book = await get_user_book(db, user_book_id)
    if db_user_book:
        for field, value in user_book_update.dict().items():
            setattr(db_user_book, field, value)
        await db.commit()
        await db.refresh(db_user_book)
    return db_user_book


async def delete_user_book(db: AsyncSession, user_book_id: int):
    db_user_book = await get_user_book(db, user_book_id)
    if db_user_book:
        await db.delete(db_user_book)
        await db.commit()
    return db_user_book
