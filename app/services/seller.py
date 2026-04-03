from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.schemas.seller import SellerCreate
from passlib.context import CryptContext
from app.database.models import Seller
from app.utils import generate_access_token

password_context = CryptContext(schemes=["argon2"], deprecated="auto")

class SellerService:
    def __init__(self, session: Session): # type: ignore
        self.session  =  session

    def add(self, credentials: SellerCreate) -> Seller:
        seller = Seller(**credentials.model_dump(exclude=["password"]), # type: ignore
        password_hash=password_context.hash(credentials.password), )

        self.session.add(seller) # type: ignore
        self.session.commit()   # type: ignore
        self.session.refresh(seller)    # type: ignore

        return seller

    def token(self, email, password):
        result = self.session.execute(select(Seller).where(Seller.email == email)) # type: ignore
        seller = result.scalar()

        if not seller or not password_context.verify(password, seller.password_hash,):
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Email or Password is incorrect"
            )

        token = generate_access_token(
            data ={ "user" :{
            "name": seller.name,
            "id": seller.id,
        }}
        )

        return token