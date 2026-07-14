from src.tools.tool_registry import ToolRegistry


class ToolManager:

    def __init__(
        self,
        knowledge: dict,
    ):
        self.knowledge = knowledge

    def execute(
        self,
        tool_name: str,
    ):

        tool_class = ToolRegistry.get(tool_name)

        tool = tool_class()

        return tool.execute(
            knowledge=self.knowledge,
        )