from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


from .base import Base


class BotUser(Base):
    __tablename__ = "BotUsers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    username = Column(String(50))
    state = Column(String(32), default="main_menu")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        pass