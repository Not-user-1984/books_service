from pydantic import BaseModel
from typing import List


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    image_url: str
    title: str
    author: str
    rating: float
    description: str


class BookCreate(BookBase):
    category_id: int
    tags: List[int] = []


class Book(BookBase):
    id: int
    category: Category
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    icon_url: str
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    favorites: List[Book] = []
    cart: List[Book] = []

    class Config:
        orm_mode = True


class UserFavorite(BaseModel):
    user_id: int
    book_id: int

    class Config:
        orm_mode = True


class UserCart(BaseModel):
    user_id: int
    book_id: int

    class Config:
        orm_mode = True

