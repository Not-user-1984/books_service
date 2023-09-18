from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int


class BookBase(BaseModel):
    title: str
    rating: int
    page_count: int
    author: str
    description: str
    publisher: str
    category_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    # category: Category


class UserBookBase(BaseModel):
    user_id: int
    page_count: int
    user_title: str
    user_author: str
    user_description: str
    user_publisher: str
    is_read: bool = False
    to_read_later: bool = False
    progress: int = 0


class UserBookCreate(UserBookBase):
    pass


class UserBookResponse(UserBookBase):
    id: int


class UserBook(UserBookBase):
    id: int



class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
