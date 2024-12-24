from marshmallow import fields, validate
from schema import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

class ProductsPaginationSchema(ma.Schema):
    items = fields.List(fields.Nested(ProductSchema))
    total = fields.Integer()
    page = fields.Integer()
    per_page = fields.Integer()

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
products_pagination_schema = ProductsPaginationSchema()
