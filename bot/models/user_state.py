from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from .base import Base


class UserState(Base):
    __tablename__ = "UserStates"

    user_id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey('States.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        pass