from typing import TypedDict
from core.adapters.controller import Controller
from backoffice.plan.application.commands import RemoveTodoUseCase


class RequestObject(TypedDict):
    plan_id: str
    todo_id: str


class RemoveTodoController(Controller[RequestObject]):
    def __init__(self, use_case: RemoveTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject) -> None:
        assert isinstance(request_object["plan_id"], str)
        assert isinstance(request_object["todo_id"], str)
        await self.use_case.interact(
            {"plan_id": request_object["plan_id"], "todo_id": request_object["todo_id"]}
        )
