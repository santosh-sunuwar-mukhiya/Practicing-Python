from fastapi import APIRouter, status, HTTPException, Depends
from ..schemas.shipment import ShipmentRead, ShipmentUpdate, ShipmentCreate
from app.api.dependencies import ShipmentServiceDep
router = APIRouter(prefix="/shipment", tags=["shipment"])

@router.get("/{id}", response_model=ShipmentRead)
def get_shipment(id: int, service: ShipmentServiceDep):
    shipment = service.get(id)

    if not shipment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"shipment with id #{id} was not found."
        )

    return shipment

@router.post("/",response_model=ShipmentRead, status_code=status.HTTP_201_CREATED)
def create_shipment(shipment: ShipmentCreate, service: ShipmentServiceDep):
    return service.add(shipment)

@router.patch("/{id}", response_model=ShipmentRead)
def update_shipment(id: int, shipment_update: ShipmentUpdate, service: ShipmentServiceDep):
    update_data = shipment_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided to update",
        )
    return service.update(id, update_data)

@router.delete("/{id}")
def delete_shipment(id: int, service: ShipmentServiceDep):
    deleted = service.delete(id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"shipment with id #{id} was not Found."
        )
    return {"message": f"shipment with id #{id} is deleted."}