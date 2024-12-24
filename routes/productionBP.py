from flask import Blueprint
from controllers.productionController import get_production_summary, get_employee_summary

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/summary', methods=['GET'])(get_production_summary)
production_blueprint.route('/employee-summary', methods=['GET'])(get_employee_summary)
