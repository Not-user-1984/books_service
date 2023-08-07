from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from db.session import get_async_session as AsyncSession
import tracemalloc
tracemalloc.start()

# CRUD операции для модели Category
async def get_category_by_name(db: AsyncSession, name: str):
    stmt = select(models.Category).where(models.Category.name == name)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_category(db: AsyncSession, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(models.Category).where(models.Category.id == category_id))
    return  result.scalar_one()

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Category).offset(skip).limit(limit))
    return result.scalars().all()


# CRUD операции для модели Tag
async def get_tag_by_name(db: AsyncSession, name: str):
    stmt = select(models.Tag).where(models.Tag.name == name)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_tag(db: AsyncSession, tag: schemas.TagCreate):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    await db.commit()
    await db.refresh(db_tag)
    return db_tag


def get_tags(db: AsyncSession, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()


# CRUD операции для модели Book
async def create_book(db: AsyncSession, book: schemas.BookCreate):
    tags = []
    for tag_id in book.tags:
        db_tag = await db.execute(select(models.Tag).where(models.Tag.id == tag_id))
        tags.append(db_tag.scalar_one_or_none())
    db_book = models.Book(**book.dict(), tags=tags)
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def get_book(db: AsyncSession, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


async def get_books(db: AsyncSession, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


# CRUD операции для модели Comment
async def create_comment(db: AsyncSession, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment


async def get_comment(db: AsyncSession, comment_id: int):
    return db.query(models.Comment).filter(
        models.Comment.id == comment_id).first()


async def get_comments_by_book(db: AsyncSession, book_id: int):
    return db.query(models.Comment).filter(
        models.Comment.book_id == book_id).all()


# CRUD операции для модели User
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db: AsyncSession, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# CRUD операции для связей UserFavorite и UserCart
async def add_book_to_favorites(db: AsyncSession, user_id: int, book_id: int):
    favorite = models.UserFavorite(user_id=user_id, book_id=book_id)
    db.add(favorite)
    await db.commit()
    await db.refresh(favorite)
    return favorite


async def add_book_to_cart(db: AsyncSession, user_id: int, book_id: int):
    cart_item = models.UserCart(user_id=user_id, book_id=book_id)
    db.add(cart_item)
    await db.commit()
    await db.refresh(cart_item)
    return cart_item


async def remove_book_from_favorites(db: AsyncSession, user_id: int, book_id: int):
    favorite = await db.query(models.UserFavorite).filter(models.UserFavorite.user_id == user_id,
                                                          models.UserFavorite.book_id == book_id).first()
    if favorite:
        db.delete(favorite)
        await db.commit()
        return True
    return False


async def remove_book_from_cart(db: AsyncSession, user_id: int, book_id: int):
    cart_item = await db.query(models.UserCart).filter(
        models.UserCart.user_id == user_id,
        models.UserCart.book_id == book_id).first()
    if cart_item:
        db.delete(cart_item)
        await db.commit()
        return True
    return False
