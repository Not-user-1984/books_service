from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from db.session import get_async_session

# CRUD операции для модели Category
async def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


async def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(
        models.Category.id == category_id).first()


async def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


# CRUD операции для модели Tag
async def get_tag_by_name(db: Session, name: str):
    stmt = select(models.Tag).where(models.Tag.name == name)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    await db.commit()
    await db.refresh(db_tag)
    return db_tag


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()


# CRUD операции для модели Book
async def create_book(db: Session, book: schemas.BookCreate):
    tags = []
    for tag_id in book.tags:
        db_tag = await db.execute(select(models.Tag).where(models.Tag.id == tag_id))
        tags.append(db_tag.scalar_one_or_none())
    db_book = models.Book(**book.dict(), tags=tags)
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
    
async def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


async def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


# CRUD операции для модели Comment
async def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment


async def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(
        models.Comment.id == comment_id).first()


async def get_comments_by_book(db: Session, book_id: int):
    return db.query(models.Comment).filter(
        models.Comment.book_id == book_id).all()


# CRUD операции для модели User
async def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# CRUD операции для связей UserFavorite и UserCart
async def add_book_to_favorites(db: Session, user_id: int, book_id: int):
    favorite = models.UserFavorite(user_id=user_id, book_id=book_id)
    db.add(favorite)
    await db.commit()
    await db.refresh(favorite)
    return favorite


async def add_book_to_cart(db: Session, user_id: int, book_id: int):
    cart_item = models.UserCart(user_id=user_id, book_id=book_id)
    db.add(cart_item)
    await db.commit()
    await db.refresh(cart_item)
    return cart_item


async def remove_book_from_favorites(db: Session, user_id: int, book_id: int):
    favorite = await db.query(models.UserFavorite).filter(models.UserFavorite.user_id == user_id,
                                                          models.UserFavorite.book_id == book_id).first()
    if favorite:
        db.delete(favorite)
        await db.commit()
        return True
    return False


async def remove_book_from_cart(db: Session, user_id: int, book_id: int):
    cart_item = await db.query(models.UserCart).filter(models.UserCart.user_id == user_id,
                                                       models.UserCart.book_id == book_id).first()
    if cart_item:
        db.delete(cart_item)
        await db.commit()
        return True
    return False
