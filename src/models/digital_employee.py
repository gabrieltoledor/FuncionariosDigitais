from src.services.knowledge import load_knowledge
from src.services.memory import MemoryService
from src.services.llm import ask_llm
from src.tools.tool_manager import ToolManager


class DigitalEmployee:

    def __init__(
        self,
        company: str,
        config: dict,
    ):
        self.company = company
        self.config = config

        self.role = config["role"]

        self.knowledge = load_knowledge(company)

    def chat(
        self,
        user_id: str,
        message: str,
    ) -> str:

        memory = MemoryService(
            conversation_id=f"{self.company}_{user_id}"
        )

        history = memory.load_history()

        tool_manager = ToolManager(
            knowledge=self.knowledge,
        )

        if message == "teste_tool":
            return tool_manager.execute(
                "get_specialties",
            )

        response = ask_llm(
            question=message,
            knowledge=self.knowledge,
            history=history,
        )

        memory.add_message("user", message)
        memory.add_message("assistant", response)

        return response