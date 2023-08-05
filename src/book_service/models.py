from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from db.base import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", back_populates="category")


class Tag(Base):
    __tablename__ = "tags"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Book(Base):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String, index=True)
    author = Column(String)
    rating = Column(Float)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="books")
    tags = relationship("Tag", secondary="book_tags")
    comments = relationship("Comment", back_populates="book")



class BookTag(Base):
    __tablename__ = "book_tags"
    __table_args__ = {'extend_existing': True}    
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)


class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="comments")


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    icon_url = Column(String)
    name = Column(String)
    favorites = relationship("Book", secondary="user_favorites")
    cart = relationship("Book", secondary="user_cart")


class UserFavorite(Base):
    __tablename__ = "user_favorites"
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)


class UserCart(Base):
    __tablename__ = "user_cart"
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
