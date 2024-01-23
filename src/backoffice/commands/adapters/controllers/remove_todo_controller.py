from typing import TypedDict
from core.adapters import Controller
from backoffice.commands.application.use_cases import RemoveTodoUseCase


class RequestObject(TypedDict):
    id: str


class RemoveTodoController(Controller[RequestObject]):
    def __init__(self, use_case: RemoveTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        id = request_object.get("id")
        await self.use_case.interact({"id": id})
