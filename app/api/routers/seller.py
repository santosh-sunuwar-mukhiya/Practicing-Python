from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import  OAuth2PasswordRequestForm

from app.api.dependencies import SellerServiceDep
from app.api.schemas.seller import SellerRead, SellerCreate

router = APIRouter(prefix="/seller", tags=["seller"])

# Register a Seller.
@router.post("/signup", response_model=SellerRead)
def register_seller(seller: SellerCreate, service: SellerServiceDep):
    return service.add(seller)

# Login a Seller
@router.post("/token")
def login_seller(request_form: Annotated[OAuth2PasswordRequestForm, Depends()], service: SellerServiceDep):
    token = service.token(request_form.username, request_form.password)
    return {"access_token": token, "token_type": "bearer"}
