from sqlalchemy.orm import Session
from app.api.schemas.seller import SellerCreate
from passlib.context import CryptContext
from app.database.models import Seller

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class SellerService:
    def __init__(self, session: Session):
        self.session  =  Session

    def add(self, credentials: SellerCreate) -> Seller:
        seller = Seller(**credentials.model_dump(exclude=["password"]),
        password_hash=password_context.hash(credentials.password), )

        self.session.add(seller)
        self.session.commit()
        self.session.refresh(seller)

        return seller
