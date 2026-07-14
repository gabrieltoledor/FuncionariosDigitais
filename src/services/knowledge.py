import json
from pathlib import Path


def load_knowledge(company: str):

    base_path = Path(f"clientes/{company}")

    empresa = json.loads(
        (base_path / "empresa.json").read_text(encoding="utf-8")
    )

    medicos = json.loads(
        (base_path / "medicos.json").read_text(encoding="utf-8")
    )

    especialidades = json.loads(
        (base_path / "especialidades.json").read_text(encoding="utf-8")
    )

    faq = json.loads(
        (base_path / "faq.json").read_text(encoding="utf-8")
    )

    prompt = (
        base_path / "prompt.md"
    ).read_text(encoding="utf-8")

    return {
        "empresa": empresa,
        "medicos": medicos,
        "especialidades": especialidades,
        "faq": faq,
        "prompt": prompt,
    }