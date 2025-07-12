from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError

from bot.models.useful_link import UsefulLink
from config import Config

from bot.models import Base

config = Config()

engine = create_engine(
    config.DATABASE_URL,
    echo=config.DEBUG,
    connect_args={"check_same_thread": False} if "sqlite" in config.DATABASE_URL else {}
)

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    try:
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        fill_useful_links()
        print(f"Tables created: {list(Base.metadata.tables.keys())}")
    except OperationalError as e:
        print(f"Database error: {e}")
        raise

def fill_useful_links():
    with Session(bind=engine) as session:
        if session.query(UsefulLink).count() == 0:
            states = [
                UsefulLink(title="УМК", link="https://umk-link.ru"),
                UsefulLink(title="ESL Brains", link="https://eslbrains.com"),
                UsefulLink(title="Lingua House", link="https://linguahouse.com"),
                UsefulLink(title="Shadowing", link="https://shadowing-technique.com"),
            ]
            session.add_all(states)
            session.commit()