from typing import TypedDict
from core.adapters import Controller
from backoffice.todo.application import GetTodoUseCase


class RequestModel(TypedDict):
    id: str


class GetTodoController(Controller[RequestModel]):
    def __init__(self, use_case: GetTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_model: RequestModel):
        id = request_model.get("id")
        assert type(id) is str
        await self.use_case.interact({"id": id})
