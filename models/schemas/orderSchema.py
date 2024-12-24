from marshmallow import fields
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchema', many=True)  # For handling multiple products

class OrderSchemaCustomer(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer = fields.Nested('CustomerSchema')
    products = fields.Nested('ProductsSchema', many=True)  # For handling multiple products

class OrdersPaginationSchema(ma.Schema):
    items = fields.List(fields.Nested(OrderSchema))
    total = fields.Integer()
    page = fields.Integer()
    per_page = fields.Integer()

# Create an instance of the OrderSchema
order_schema_customer = OrderSchemaCustomer()
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)  # For handling multiple orders

# Pagination schema instance
orders_pagination_schema = OrdersPaginationSchema()
