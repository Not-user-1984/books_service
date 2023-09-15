from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    rating = Column(Integer)
    page_count = Column(Integer)
    author = Column(String)
    description = Column(String)
    publisher = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="books")


class UserBook(Base):
    __tablename__ = "user_books"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    page_count = Column(Integer)
    user_title = Column(String)
    user_author = Column(String)
    user_description = Column(String)
    user_publisher = Column(String)
    is_read = Column(Boolean, default=False)
    to_read_later = Column(Boolean, default=False)
    progress = Column(Integer, default=0)
    user = relationship("User", back_populates="user_books")
    book = relationship("Book", back_populates="user_books")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_books = relationship("UserBook", back_populates="user")
