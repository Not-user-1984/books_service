from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from db import models
from book_service import schemas


# Create
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# Read
async def get_user(db: AsyncSession, username: str):
    user = await db.execute(
        select(models.User).where(models.User.username == username)
    )
    return user.scalar_one_or_none()


# Update
async def update_user(
    db: AsyncSession, user_id: int, user_update: schemas.UserCreate
):
    db_user = await get_user(db, user_id)
    if db_user:
        for field, value in user_update.dict().items():
            setattr(db_user, field, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user


# Delete
async def delete_user(db: AsyncSession, user_id: int):
    db_user = await get_user(db, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()
    return db_user
