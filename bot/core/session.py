from contextlib import contextmanager
from sqlalchemy.orm import Session
from .database import create_session_factory, init_db
from config import Config

# Инициализация движка и фабрики сессий
engine = init_db()
SessionLocal = create_session_factory(engine)

@contextmanager
def get_db_session():
    """Контекстный менеджер для работы с сессиями БД"""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()