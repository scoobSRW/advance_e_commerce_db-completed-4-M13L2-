from typing import List
from datetime import date
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from models.orderProduct import order_product


class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('Customers.id'))
    total_amount: Mapped[int] = mapped_column(primary_key=False)
    # Many-To-One: Order and Customer
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    # Many-To-Many: Products and Orders with no back_populates
    products: Mapped[List["Product"]] = relationship(
        "Product",
        secondary=order_product,
        back_populates="orders"
    )
