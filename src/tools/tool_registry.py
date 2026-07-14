from src.tools.implementations.get_specialties_tool import GetSpecialtiesTool


class ToolRegistry:

    _tools = {
        "get_specialties": GetSpecialtiesTool,
    }

    @classmethod
    def get(cls, tool_name: str):

        if tool_name not in cls._tools:
            raise ValueError(
                f"Ferramenta '{tool_name}' não encontrada."
            )

        return cls._tools[tool_name]