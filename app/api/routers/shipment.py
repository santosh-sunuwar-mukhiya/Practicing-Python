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
    },
]

@router.get("/{id}", response_model=ShipmentRead)
def get_shipment(id: int):
    for ship in shipment:
        if ship["id"] == id:
            return ship

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"shipment with id #{id} was not found."
    )

@router.post("/",response_model=ShipmentRead, status_code=status.HTTP_201_CREATED)
def create_shipment(create: ShipmentCreate):
    new_id = max((ship["id"] for ship in shipment),  default=0) + 1

    new_shipment = {
        "id": new_id,
        **create.model_dump(),
        "status": "placed"
    }

    shipment.append(new_shipment)

    return new_shipment

@router.patch("/{id}", response_model=ShipmentRead)
def update_shipment(id: int, update: ShipmentUpdate):
    for ship in shipment:
        if ship['id'] == id:
            update_data = update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                ship[key] = value
            return ship

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"shipment with given id #{id} was not found."
    )

@router.delete("/{id}")
def delete_shipment(id: int):
    for index, ship in enumerate(shipment):
        if ship["id"] == id:
            shipment.pop(index)
            return {"detail": f"shipment with id #{id} is deleted."}

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"shipment with given id #{id} was not found."
    )