from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import Config

# Базовый класс для моделей
Base = declarative_base()


def init_db():
    """Инициализация подключения к БД"""
    engine = create_engine(
        Config.DATABASE_URL,
        echo=Config.DEBUG,
        connect_args={"check_same_thread": False}  # Для SQLite
    )

    # Создаем таблицы
    Base.metadata.create_all(bind=engine)

    return engine


def create_session_factory(engine):
    """Создаем фабрику сессий"""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)