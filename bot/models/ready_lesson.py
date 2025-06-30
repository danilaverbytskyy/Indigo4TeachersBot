from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .base import Base


class ReadyLesson(Base):
    __tablename__ = "ReadyLessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=True)
    link = Column(String(100), nullable=False)

    def __repr__(self):
        pass