import json
from pathlib import Path


class MemoryService:

    def __init__(self, conversation_id: str):
        self.folder = Path("conversas")
        self.folder.mkdir(exist_ok=True)

        self.file = self.folder / f"{conversation_id}.json"

    def load_history(self):
        if not self.file.exists():
            return []

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_history(self, history):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

    def add_message(self, role, content):
        history = self.load_history()

        history.append({
            "role": role,
            "content": content
        })

        self.save_history(history)

    def clear(self):
        self.save_history([])