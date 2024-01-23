from typing import TypedDict
from core.adapters import Controller
from backoffice.queries.application.use_cases import GetTodoUseCase


class RequestObject(TypedDict):
    id: str


class GetTodoController(Controller[RequestObject]):
    def __init__(self, use_case: GetTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        id = request_object.get("id")
        assert type(id) is str
        await self.use_case.interact({"id": id})
