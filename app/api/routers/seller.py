from fastapi import APIRouter

from app.api.dependencies import SellerServiceDep
from app.api.schemas.seller import SellerRead, SellerCreate

router = APIRouter(prefix="/seller", tags=["seller"])

@router.post("/signup", response_model=SellerRead)
def register_seller(seller: SellerCreate, service: SellerServiceDep):
    return service.add(seller)