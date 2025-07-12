from sqlalchemy.orm import Session

from bot.core.database import engine
from bot.models import BotUser


def set_user_state(user_id: int, state: str):
    with Session(autoflush=False, bind=engine) as db:
        bot_user = db.query(BotUser).filter_by(user_id=user_id).first()
        bot_user.state = state
        db.commit()

def get_user_state(user_id: int) -> str:
    with Session(autoflush=False, bind=engine) as db:
        bot_user = db.query(BotUser).filter_by(user_id=user_id).first()
        return bot_user.state