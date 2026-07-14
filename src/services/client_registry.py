import json
from pathlib import Path

REGISTRY_FILE = Path("clientes/clientes.json")


def load_registry():
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_company_by_phone(phone: str):
    registry = load_registry()

    return registry.get(phone)