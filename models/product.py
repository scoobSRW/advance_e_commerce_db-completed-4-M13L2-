from typing import List
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from models.orderProduct import order_product

class Product(Base):
    __tablename__ = 'products'

    # Columns
    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    # Many-To-Many: Products and Orders
    orders: Mapped[List["Order"]] = relationship(
        "Order",
        secondary=order_product,
        back_populates="products"
    )

    # Use string literal for the back reference to Production
    productions: Mapped[List["Production"]] = relationship(
        "Production",
        back_populates="product"
    )
