from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


from .base import Base


class UsefulLink(Base):
    __tablename__ = "UsefulLinks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    link = Column(String(100), nullable=False)

    def __repr__(self):
        pass