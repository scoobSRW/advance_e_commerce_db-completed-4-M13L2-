from sqlalchemy import select, func
from sqlalchemy.orm import Session
from database import db
from models.production import Production
from models.product import Product

def get_production_summary(date):
    with Session(db.engine) as session:
        query = (
            select(Product.product_name, func.sum(Production.quantity_produced).label("total_quantity_produced"))
            .join(Product, Production.product_id == Product.product_id)
            .where(Production.production_date == date)
            .group_by(Product.product_name)
        )
        result = session.execute(query).all()
        return [{"product_name": row[0], "total_quantity_produced": row[1]} for row in result]

def get_employee_summary():
    with Session(db.engine) as session:
        query = (
            select(Production.employee_name, func.sum(Production.quantity_produced).label("total_quantity"))
            .group_by(Production.employee_name)
        )
        result = session.execute(query).all()
        return [{"employee_name": row[0], "total_quantity": row[1]} for row in result]

