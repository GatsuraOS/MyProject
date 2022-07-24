from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models import Product, create_session
from Schemas import ProductSchema
from Schemas import ProductInDBSchema


class CRUDProduct:

    @staticmethod
    @create_session
    def add(product: ProductSchema, session: Session = None) -> ProductInDBSchema | None:
        product = Product(
            **product.__dict__
        )
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(product)
            return ProductInDBSchema(**product.__dict__)

    @staticmethod
    @create_session
    def get(product_id: int, session: Session = None) -> Product | None:
        product = session.execute(
            select(Product).where(Product.id == product_id)
        )
        product = product.first()
        if product:
            return product[0]

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[Product]:
        products = session.execute(
            select(Product)
        )
        return [product[0] for product in products.all()]

    @staticmethod
    @create_session
    def delete(product_id: int, session: Session = None) -> None:
        session.execute(
            delete(Product).where(Product.id == product_id)
        )
        session.commit()

