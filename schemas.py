from flask_marshmallow import Marshmallow
from marshmallow import fields, validates, ValidationError
from models import Employee

ma = Marshmallow()

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee
        load_instance = True

    id = ma.auto_field(dump_only=True)
    fullName = ma.auto_field(required=True)
    email = ma.auto_field(required=True)
    position = ma.auto_field(required=True)
    salary = ma.auto_field(required=True)
    dateOfJoining = fields.Date(required=True)

    @validates("salary")
    def validate_salary(self, value):
        if value <= 0:
            raise ValidationError("Salary must be positive.")
