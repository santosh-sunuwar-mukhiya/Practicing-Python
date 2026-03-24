from sqlmodel import SQLModel, Field
from datetime import UTC, datetime

class Shipment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    content: str
    weight: float = Field(le=25)
    destination: int
    status: str
    estimated_delivery: datetime
