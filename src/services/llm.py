from openai import OpenAI

from src.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(
    question: str,
    knowledge: dict,
    history: list,
) -> str:

    system_prompt = f"""
{knowledge["prompt"]}

EMPRESA:
{knowledge["empresa"]}

MÉDICOS:
{knowledge["medicos"]}

ESPECIALIDADES:
{knowledge["especialidades"]}

FAQ:
{knowledge["faq"]}

INSTRUÇÕES:

- Você é a recepcionista virtual desta clínica.
- Utilize apenas as informações fornecidas acima.
- Nunca invente informações.
- Se não souber responder, informe educadamente que irá encaminhar o paciente para a equipe da clínica.
- Responda sempre em português do Brasil.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages,
    )

    return response.output_text