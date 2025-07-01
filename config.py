import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
    DEBUG = os.getenv("DEBUG", "False") == "True"

    # Путь к базе данных
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Настройки Alembic
    ALEMBIC_CONFIG = os.path.join(BASE_DIR, "migrations", "alembic.ini")