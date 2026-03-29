from sqlalchemy.orm import Session


from app.database.models import Shipment
from app.api.schemas.shipment import ShipmentCreate
from datetime import UTC, datetime

class ShipmentService:
    def __init__(self, session: Session):
        self.session = session

    # shipment get by id
    def get(self, id: int):
        return self.session.get(Shipment, id)

    # Add a new shipment
    def add(self, shipment_create: ShipmentCreate):
        new_shipment = Shipment(
            **shipment_create.model_dump(),
            placed="placed",
            estimated_delivery=datetime.now(UTC)
        )
        self.session.add(new_shipment)
        self.session.commit()
        self.session.refresh(new_shipment)
        return new_shipment

    # Update shipment
    def update(self, id: int, shipment_update: dict):
        shipment = self.get(id)
        shipment.sqlmodel_update(shipment_update)
        self.session.add(shipment)
        self.session.commit()
        self.session.refresh(shipment)
        return shipment

    # Delete shipment
    def delete(self, id: int):
        shipment = self.get(id)
        if shipment is None:
            return False

        self.session.delete(shipment)
        self.session.commit()

        return True


