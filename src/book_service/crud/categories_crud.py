from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import models
from book_service import schemas
from fastapi import HTTPException


# Create
async def create_category(db: AsyncSession, category: schemas.CategoryCreate):
    existing_category = await db.execute(
        select(models.Category).where(models.Category.name == category.name)
    )

    if existing_category.scalar_one_or_none():
        raise HTTPException(
            status_code=409,
            detail="Category with the same name already exists",
        )

    db_category = models.Category(**category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


# Read
async def get_category(db: AsyncSession, category_id: int):
    category = await db.execute(
        select(models.Category).where(models.Category.id == category_id)
    )
    return category.scalar_one_or_none()


# Update
async def update_category(
    db: AsyncSession, category_id: int, category_update: schemas.CategoryCreate
):
    db_category = await get_category(db, category_id)

    if db_category:
        for field, value in category_update.dict().items():
            setattr(db_category, field, value)
        await db.commit()
        await db.refresh(db_category)
    return db_category


# Delete
async def delete_category(db: AsyncSession, category_id: int):
    db_category = await get_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category
