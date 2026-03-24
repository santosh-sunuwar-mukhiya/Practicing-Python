from fastapi import APIRouter, status, HTTPException
from ..schemas.shipment import ShipmentRead, ShipmentUpdate, ShipmentCreate
router = APIRouter(prefix="/shipment", tags=["shipment"])

shipment = [
    {
        "id": 1,
        "content": "my book",
        "weight": 2.5,
        "destination":1120,
        "status": "placed"
    }
]

@router.get("/", response_model=ShipmentRead)
def get_shipment(id: int):
    for ship in shipment:
        if ship["id"] == id:
            return ship

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"shipment with id #{id} was not found."
    )