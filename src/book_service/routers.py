from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.session import get_async_session as get_db

from . import crud, models, schemas

router = APIRouter()


# Роутеры для Category
@router.post("/categories/", response_model=schemas.Category)
async def create_category(
        category: schemas.CategoryCreate,
        db: Session = Depends(get_db)):
    db_category = await crud.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return await crud.create_category(db=db, category=category)


@router.get("/categories/{category_id}", response_model=schemas.Category)
async def get_category(category_id: int, db: get_db = Depends(get_db)):
    category = await crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/categories/", response_model=list[schemas.Category])
async def get_categories(
    skip: int = 0,
    limit: int = 100,
    db: get_db = Depends(get_db)
):
    categories = await crud.get_categories(db, skip=skip, limit=limit)
    return categories


# Роутеры для  Tag
@router.post("/tags/", response_model=schemas.Tag)
async def create_tag(
    tag: schemas.TagCreate,
    db: get_db = Depends(get_db)
):
    db_tag = await crud.get_tag_by_name(db, name=tag.name)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return await crud.create_tag(db=db, tag=tag)


@router.get("/tags/", response_model=list[schemas.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.get_tags(db=db, skip=skip, limit=limit)
    return tags


@router.post("/books/", response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return await crud.create_book(db=db, book=book)


@router.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books


@router.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)


@router.get("/comments/", response_model=list[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments(db=db, skip=skip, limit=limit)
    return comments


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}/favorites/", response_model=list[schemas.Book])
def read_user_favorites(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_favorites(db=db, user_id=user_id)


@router.get("/users/{user_id}/cart/", response_model=list[schemas.Book])
def read_user_cart(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_cart(db=db, user_id=user_id)
