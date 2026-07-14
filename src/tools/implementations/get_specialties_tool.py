from src.tools.base_tool import BaseTool


class GetSpecialtiesTool(BaseTool):

    name = "get_specialties"

    description = "Retorna as especialidades da clínica."

    def execute(
        self,
        **context,
    ):

        knowledge = context["knowledge"]

        return knowledge["especialidades"]