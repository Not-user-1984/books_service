from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from book_service.crud import (books_crud, categories_crud, user_books_crud,
                               users_crud)
from db.database import get_async_session

from . import schemas

router = APIRouter()


# Маршруты для модели Category
@router.post("/categories/",
             response_model=schemas.Category)
async def create_category_endpoint(
    category: schemas.CategoryCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await categories_crud.create_category(db, category)


@router.get("/categories/{category_id}",
            response_model=schemas.Category)
async def read_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await categories_crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/categories/{category_id}",
            response_model=schemas.Category)
async def update_category_endpoint(
    category_id: int,
    category_update: schemas.CategoryCreate,
    db: AsyncSession = Depends(get_async_session)
):
    category = await categories_crud.update_category(
        db, category_id, category_update)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/categories/{category_id}",
               response_model=schemas.Category)
async def delete_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await categories_crud.delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# Маршруты для модели Book
@router.post("/books/", response_model=schemas.Book)
async def create_book_endpoint(
    book: schemas.BookCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await books_crud.create_book(db, book)


@router.get("/books/{book_id}", response_model=schemas.Book)
async def read_book_endpoint(
    book_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    book = await books_crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=schemas.Book)
async def update_book_endpoint(
    book_id: int,
    book_update: schemas.BookCreate,
    db: AsyncSession = Depends(get_async_session)
):
    book = await books_crud.update_book(db, book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}",
               response_model=schemas.Book)
async def delete_book_endpoint(
    book_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    book = await books_crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# Маршруты для модели UserBook
@router.post("/user_books/", response_model=schemas.UserBookResponse)
async def create_user_book_endpoint(
    user_book: schemas.UserBookCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await user_books_crud.create_user_book(db, user_book)


@router.get("/user_books/{user_book_id}", response_model=schemas.UserBook)
async def read_user_book_endpoint(
    user_book_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    user_book = await user_books_crud.get_user_book(db, user_book_id)
    if not user_book:
        raise HTTPException(status_code=404, detail="UserBook not found")
    return user_book


@router.get("/user_books", response_model=list[schemas.UserBook])
async def read_user_books_endpoint(
    user_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    user_book = await user_books_crud.get_user_books(db, user_id)
    if not user_book:
        raise HTTPException(status_code=404, detail="UserBook not found")
    return user_book


@router.put("/user_books/{user_book_id}",
            response_model=schemas.UserBook)
async def update_user_book_endpoint(
    user_book_id: int,
    user_book_update: schemas.UserBookCreate,
    db: AsyncSession = Depends(get_async_session)
):
    user_book = await user_books_crud.update_user_book(
        db, user_book_id, user_book_update)
    if not user_book:
        raise HTTPException(status_code=404, detail="UserBook not found")
    return user_book


@router.delete("/user_books/{user_book_id}",
               response_model=schemas.UserBook)
async def delete_user_book_endpoint(
    user_book_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    user_book = await user_books_crud.delete_user_book(db, user_book_id)
    if not user_book:
        raise HTTPException(status_code=404, detail="UserBook not found")
    return user_book


# Маршруты для модели User
@router.post("/users/", response_model=schemas.User)
async def create_user_endpoint(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await users_crud.create_user(db, user)


@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user_endpoint(
    user_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    user = await users_crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=schemas.User)
async def update_user_endpoint(
    user_id: int,
    user_update: schemas.UserCreate,
    db: AsyncSession = Depends(get_async_session)
):
    user = await users_crud.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user_endpoint(
    user_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    user = await users_crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
