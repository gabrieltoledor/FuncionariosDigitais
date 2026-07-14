from pathlib import Path


EMPLOYEES_PATH = Path("clientes")


class EmployeeRegistry:

    @staticmethod
    def get(company: str, employee: str) -> Path:

        return (
            EMPLOYEES_PATH
            / company
            / "employees"
            / f"{employee}.json"
        )

    @staticmethod
    def exists(company: str, employee: str) -> bool:

        return EmployeeRegistry.get(
            company,
            employee,
        ).exists()

    @staticmethod
    def list(company: str) -> list[str]:

        employees_path = (
            EMPLOYEES_PATH
            / company
            / "employees"
        )

        if not employees_path.exists():
            return []

        return [
            file.stem
            for file in employees_path.glob("*.json")
        ]