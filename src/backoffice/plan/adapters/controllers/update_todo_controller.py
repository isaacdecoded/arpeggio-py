from typing import TypedDict
from core.adapters import Controller
from backoffice.plan.application.commands import UpdateTodoUseCase


class RequestObject(TypedDict):
    plan_id: str
    todo_id: str
    description: str


class UpdateTodoController(Controller[RequestObject]):
    def __init__(self, use_case: UpdateTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject) -> None:
        assert isinstance(request_object["plan_id"], str)
        assert isinstance(request_object["todo_id"], str)
        assert isinstance(request_object["description"], str)
        await self.use_case.interact(
            {
                "plan_id": request_object["plan_id"],
                "todo_id": request_object["todo_id"],
                "description": request_object["description"],
            }
        )
