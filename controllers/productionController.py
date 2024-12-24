from flask import jsonify, request
from models.schemas.productionSchema import (
    production_schema,
    production_summary_schema,
    employee_production_schema,
)
from marshmallow import ValidationError
from services import productionService

def get_production_summary():
    try:
        date = request.args.get('date', None)
        if not date:
            return jsonify({"error": "Date is required"}), 400

        summary = productionService.get_production_summary(date)
        return jsonify(production_summary_schema.dump(summary)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_employee_summary():
    try:
        summary = productionService.get_employee_summary()
        return jsonify(employee_production_schema.dump(summary)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
