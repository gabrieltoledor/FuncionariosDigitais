from src.models.digital_employee import DigitalEmployee

from src.services.employee_registry import EmployeeRegistry
from src.services.employee_loader import EmployeeLoader


class EmployeeFactory:

    @staticmethod
    def create(
        company: str,
        employee: str,
    ) -> DigitalEmployee:

        path = EmployeeRegistry.get(
            company,
            employee,
        )

        if not path.exists():
            raise FileNotFoundError(
                f"Funcionário '{employee}' não encontrado para a empresa '{company}'."
            )

        config = EmployeeLoader.load(path)

        return DigitalEmployee(
    company=company,
    config=config,
)