from typing import TypedDict
from core.adapters import Controller
from backoffice.commands.application.use_cases import CreateTodoUseCase


class RequestObject(TypedDict):
    name: str


class CreateTodoController(Controller[RequestObject]):
    def __init__(self, use_case: CreateTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        name = request_object.get("name")
        assert type(name) is str
        await self.use_case.interact({"name": name})
