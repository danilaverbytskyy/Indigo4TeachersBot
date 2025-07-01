from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import now

from .base import Base


class State(Base):
    __tablename__ = "States"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)

    def __repr__(self):
        pass