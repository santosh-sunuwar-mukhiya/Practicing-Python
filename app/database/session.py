from sqlmodel import SQLModel, Session, create_engine
from app.config import db_settings

# check_same_thread=False is strictly required for FastAPI + SQLite
engine = create_engine(
    db_settings.DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

def create_db_tables():
    from app.database.models import Shipment  # noqa: F401
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

