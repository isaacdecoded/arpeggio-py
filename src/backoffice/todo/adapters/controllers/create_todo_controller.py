from typing import TypedDict
from core.adapters import Controller
from backoffice.todo.application import CreateTodoUseCase


class RequestModel(TypedDict):
    name: str


class CreateTodoController(Controller[RequestModel]):
    def __init__(self, use_case: CreateTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_model: RequestModel):
        name = request_model.get("name")
        assert type(name) is str
        await self.use_case.interact({"name": name})
