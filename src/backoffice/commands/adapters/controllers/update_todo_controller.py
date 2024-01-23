from typing import TypedDict
from core.adapters import Controller
from backoffice.commands.application.use_cases import UpdateTodoUseCase


class RequestObject(TypedDict):
    id: str
    name: str


class UpdateTodoController(Controller[RequestObject]):
    def __init__(self, use_case: UpdateTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        id = request_object.get("id")
        name = request_object.get("name")
        assert type(id) is str
        assert type(name) is str
        await self.use_case.interact(
            {
                "id": id,
                "name": name,
            }
        )
