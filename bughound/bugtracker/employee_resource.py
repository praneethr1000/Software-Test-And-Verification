from import_export import resources

from .employee_model import Employee


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee