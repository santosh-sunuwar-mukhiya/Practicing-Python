from fastapi import Depends
from app.database.session import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from app.services.shipment import ShipmentService

SessionDep = Annotated[Session, Depends(get_session)]

# Shipment Service Dependency
def get_shipment_service(session:SessionDep):
    return ShipmentService(session)

# Shipment Service Dependency Annotation
ShipmentServiceDep = Annotated[ShipmentService, Depends(get_shipment_service)]
