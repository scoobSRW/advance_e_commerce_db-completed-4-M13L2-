from marshmallow import fields
from schema import ma

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False)
    product_id = fields.Integer(required=True)
    employee_name = fields.String(required=True)
    production_date = fields.Date(required=True)
    quantity_produced = fields.Integer(required=True)

class ProductionSummarySchema(ma.Schema):
    product_name = fields.String(required=True)  # Name of the product
    total_quantity_produced = fields.Integer(required=True)  # Total quantity for the date

class EmployeeProductionSchema(ma.Schema):
    employee_name = fields.String(required=True)  # Name of the employee
    total_quantity = fields.Integer(required=True)  # Total quantity produced by the employee

# Instances of the schemas
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)
production_summary_schema = ProductionSummarySchema(many=True)
employee_production_schema = EmployeeProductionSchema(many=True)
