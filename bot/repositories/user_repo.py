from sqlalchemy.orm import Session
from bot.core.database import engine
from bot.models.bot_user import BotUser
from bot.core.session import get_db_session
from contextlib import contextmanager

class UserRepository:
    @staticmethod
    @contextmanager
    def get_db():
        with get_db_session() as session:
            yield session


    @classmethod
    def get_or_create_user(cls, user_id: int, username: str, full_name: str):
        with cls.get_db() as session:
            user = session.query(BotUser).filter_by(user_id=user_id).first()
            if not user:
                user = BotUser(user_id=user_id, username=username, full_name=full_name)
                session.add(user)
                session.commit()
            return user

    @classmethod
    def get_user_by_id(cls, user_id: int):
        with cls.get_db() as session:
            return session.query(BotUser).filter_by(user_id=user_id).first()

    @classmethod
    def set_user_state(cls, user_id: int, state: str):
        with Session(autoflush=False, bind=engine) as db:
            bot_user = cls.get_user_by_id(user_id)
            bot_user.state = state
            db.commit()

    @classmethod
    def get_user_state(cls, user_id: int) -> str:
       bot_user = cls.get_user_by_id(user_id)
       return bot_user.state