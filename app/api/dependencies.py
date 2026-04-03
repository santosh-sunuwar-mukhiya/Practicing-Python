from fastapi import Depends, HTTPException, status

from app.core.security import oauth2_scheme
from app.database.models import Seller
from app.database.session import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.services.seller import SellerService
from app.services.shipment import ShipmentService
from app.utils import decode_access_token

SessionDep = Annotated[Session, Depends(get_session)]

def get_access_token(token: Annotated[str, Depends(oauth2_scheme)]):
    data = decode_access_token(token)

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
        )

    return data

def get_current_seller(token_data: Annotated[dict, Depends(get_access_token)], session: SessionDep):
    return session.get(Seller, token_data["user"]["id"])

# Shipment Service Dependency
def get_shipment_service(session:SessionDep):
    return ShipmentService(session)

# Seller Service Dependency
def get_seller_service(session: SessionDep):
    return SellerService(session)

# Seller Dep
SellerDep = Annotated[ShipmentService, Depends(get_current_seller)]
# Shipment Service Dependency Annotation
ShipmentServiceDep = Annotated[ShipmentService, Depends(get_shipment_service)]

# Seller Service Dependency Annotation
SellerServiceDep = Annotated[SellerService, Depends(get_seller_service)]
