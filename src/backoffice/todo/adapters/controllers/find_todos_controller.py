from typing import TypedDict
from core.adapters import Controller
from backoffice.todo.application import FindTodosUseCase


class RequestModel(TypedDict):
    name: str | None
    limit: int
    offset: int


class FindTodosController(Controller[RequestModel]):
    def __init__(self, use_case: FindTodosUseCase):
        self.use_case = use_case

    async def execute(self, request_model: RequestModel):
        name = request_model.get("name")
        limit = request_model.get("limit")
        offset = request_model.get("offset")
        assert type(limit) is int
        assert type(offset) is int
        await self.use_case.interact(
            {
                "name": name,
                "limit": limit,
                "offset": offset,
            }
        )
