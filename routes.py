from flask import Blueprint, request, jsonify
from models import db, Employee
from schemas import EmployeeSchema
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Create a new employee

@routes.route("/employees", methods=["POST"])
def create_employee():
    try:
        data = employee_schema.load(request.json)  # Validate and load data
        
        db.session.add(data)
        db.session.commit()
        return employee_schema.jsonify(data), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# List all employees 

@routes.route("/employees", methods=["GET"])
def get_employees():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    employees = Employee.query.paginate(page=page, per_page=limit, error_out=False).items
    return employees_schema.jsonify(employees), 200

# Get an employee by ID

@routes.route("/employees/<id>", methods=["GET"])
def get_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return employee_schema.jsonify(emp), 200

# Update employee details

@routes.route("/employees/<id>", methods=["PUT"])
def update_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    try:
        data = request.json
        if "email" in data and data["email"] != emp.email:
            if Employee.query.filter_by(email=data["email"]).first():
                return jsonify({"error": "Email already exists"}), 400

        for key, value in data.items():
            setattr(emp, key, value)

        db.session.commit()
        return employee_schema.jsonify(emp), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete an employee

@routes.route("/employees/<id>", methods=["DELETE"])
def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"}), 200
