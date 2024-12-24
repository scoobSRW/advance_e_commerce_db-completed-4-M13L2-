from typing import List
from sqlalchemy import ForeignKey, Integer, String, Date
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from models.product import Product

class Production(Base):
    __tablename__ = 'production'

    # Correct column types and relationships
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.product_id'), nullable=False)  # Fixed ForeignKey reference
    employee_name: Mapped[str] = mapped_column(String(255), nullable=False)  # Added length for VARCHAR
    production_date: Mapped[date] = mapped_column(nullable=False)
    quantity_produced: Mapped[int] = mapped_column(nullable=False)

    # Many-to-One relationship with Product
    product: Mapped["Product"] = relationship("Product", back_populates="productions")


