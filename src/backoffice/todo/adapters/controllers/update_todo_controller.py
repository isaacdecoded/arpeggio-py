from typing import TypedDict
from core.adapters import Controller
from backoffice.todo.application import UpdateTodoUseCase


class RequestModel(TypedDict):
    id: str
    name: str


class UpdateTodoController(Controller[RequestModel]):
    def __init__(self, use_case: UpdateTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_model: RequestModel):
        id = request_model.get("id")
        name = request_model.get("name")
        assert type(id) is str
        assert type(name) is str
        await self.use_case.interact(
            {
                "id": id,
                "name": name,
            }
        )
