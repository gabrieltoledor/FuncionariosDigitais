import json
from pathlib import Path


class EmployeeLoader:

    @staticmethod
    def load(path: Path) -> dict:

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)