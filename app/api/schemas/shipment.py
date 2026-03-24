from pydantic import BaseModel, Field
from datetime import datetime

class BaseShipment(BaseModel):
    content: str = Field(max_length=100)
    weight: float = Field(lt=25)
    destination: int

class ShipmentRead(BaseShipment):
    id: int
    status: str

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    status: str | None = Field(default=None)