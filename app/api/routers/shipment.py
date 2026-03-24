from fastapi import APIRouter, status, HTTPException
from ..schemas.shipment import ShipmentRead, ShipmentUpdate, ShipmentCreate
from app.database.session import SessionDep
from app.database.models import Shipment
from datetime import UTC, datetime
router = APIRouter(prefix="/shipment", tags=["shipment"])

# shipment = [
#     {
#         "id": 1,
#         "content": "my book",
#         "weight": 2.5,
#         "destination":1120,
#         "status": "placed"
#     },
# ]

@router.get("/{id}", response_model=ShipmentRead)
def get_shipment(id: int, session: SessionDep):
    shipment = session.get(Shipment, id)

    if not shipment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"shipment with id #{id} was not found."
        )

    return shipment

@router.post("/",response_model=ShipmentRead, status_code=status.HTTP_201_CREATED)
def create_shipment(create: ShipmentCreate, session: SessionDep):
    shipment = Shipment(**create.model_dump(), status="placed", estimated_delivery=datetime.now(UTC))
    session.add(shipment)
    session.commit()
    session.refresh(shipment)

    return shipment

@router.patch("/{id}", response_model=ShipmentRead)
def update_shipment(id: int, update: ShipmentUpdate, session: SessionDep):
    shipment = session.get(Shipment, id)

    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"shipment with given id #{id} was not found."
        )

    update_data = update.model_dump(exclude_unset=True)
    shipment.sqlmodel_update(update_data)
    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment

@router.delete("/{id}")
def delete_shipment(id: int, session: SessionDep):
    shipment = session.get(Shipment, id)

    if not shipment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"shipment with given id #{id} was not found."
        )

    session.delete(shipment)
    session.commit()

    return {"message": f"shipment with id #{id} is deleted."}