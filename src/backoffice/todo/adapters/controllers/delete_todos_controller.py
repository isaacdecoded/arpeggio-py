from typing import TypedDict
from core.adapters import Controller
from backoffice.todo.application import DeleteTodoUseCase


class RequestModel(TypedDict):
    id: str | None


class DeleteTodosController(Controller[RequestModel]):
    def __init__(self, use_case: DeleteTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_model: RequestModel | None = None):
        id = None
        if request_model:
            id = request_model.get("id")
        await self.use_case.interact({"id": id})
