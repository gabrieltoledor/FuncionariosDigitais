from fastapi import FastAPI
from pydantic import BaseModel

from src.models.digital_employee import DigitalEmployee

app = FastAPI(
    title="Funcionários Digitais",
    version="0.1.0"
)


class Message(BaseModel):
    message: str
    user_id: str


@app.get("/")
def home():
    return {
        "status": "online",
        "empresa": "Funcionários Digitais"
    }


@app.post("/chat")
def chat(data: Message):

    employee = DigitalEmployee(
        company="clinica_demo",
        role="recepcionista",
    )

    response = employee.chat(
        user_id=data.user_id,
        message=data.message,
    )

    return {
        "response": response
    }