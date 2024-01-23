from typing import TypedDict
from core.adapters import Controller
from backoffice.queries.application.use_cases import FindTodosUseCase


class RequestObject(TypedDict):
    name: str | None
    limit: int
    offset: int


class FindTodosController(Controller[RequestObject]):
    def __init__(self, use_case: FindTodosUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        name = request_object.get("name")
        limit = request_object.get("limit")
        offset = request_object.get("offset")
        assert type(limit) is int
        assert type(offset) is int
        await self.use_case.interact(
            {
                "name": name,
                "limit": limit,
                "offset": offset,
            }
        )
