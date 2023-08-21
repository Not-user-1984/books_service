from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base


class PreBase:
    id = Column(Integer, primary_key=True, index=True,)


Base = declarative_base(cls=PreBase)
