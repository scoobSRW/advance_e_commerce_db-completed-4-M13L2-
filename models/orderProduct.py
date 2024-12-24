from database import db, Base

# Association table for the many-to-many relationshp
order_product = db.Table(
    'Order_Product',
    Base.metadata,
    db.Column('order_id', db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.ForeignKey('products.product_id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False),
    db.Column('price', db.Float, nullable=False)
)