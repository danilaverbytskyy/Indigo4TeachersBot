from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from config import Config
import os

# Импортируем Base ИЗ МОДЕЛЕЙ (а не создаем здесь)
from bot.models import Base

# Инициализация конфига
config = Config()

# Создаем движок
engine = create_engine(
    config.DATABASE_URL,
    echo=config.DEBUG,
    connect_args={"check_same_thread": False} if "sqlite" in config.DATABASE_URL else {}
)

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Создает все таблицы в базе данных"""
    try:
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        print(f"Tables created: {list(Base.metadata.tables.keys())}")
    except OperationalError as e:
        print(f"Database error: {e}")
        raise