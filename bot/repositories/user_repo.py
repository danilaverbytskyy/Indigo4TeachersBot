from sqlalchemy.orm import Session
from bot.core.database import engine
from bot.models.bot_user import BotUser
from contextlib import contextmanager

class UserRepository:
    @classmethod
    def get_user_by_id(cls, user_id: int):
        with Session(autoflush=False, bind=engine) as db:
            return db.query(BotUser).filter_by(user_id=user_id).first()

    @classmethod
    def set_user_state(cls, user_id: int, state: str):
        with Session(autoflush=False, bind=engine) as db:
            bot_user = db.query(BotUser).filter_by(user_id=user_id).first()
            bot_user.state = state
            db.commit()

    @classmethod
    def get_user_state(cls, user_id: int) -> str:
        with Session(autoflush=False, bind=engine) as db:
           bot_user = db.query(BotUser).filter_by(user_id=user_id).first()
           return bot_user.state