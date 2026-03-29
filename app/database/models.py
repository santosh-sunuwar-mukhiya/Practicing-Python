from pydantic import EmailStr
from sqlmodel import SQLModel, Field
from datetime import UTC, datetime

class Shipment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    content: str
    weight: float = Field(le=25)
    destination: int
    status: str = "pending"
    estimated_delivery: datetime

class Seller(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    name: str

    email: EmailStr
    password_hash: str