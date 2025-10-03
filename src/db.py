from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import os

# Use a local SQLite file in the workspace for development
BASE_DIR = Path(__file__).parent
DB_URL = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'app.db'}")

engine = create_engine(DB_URL, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
