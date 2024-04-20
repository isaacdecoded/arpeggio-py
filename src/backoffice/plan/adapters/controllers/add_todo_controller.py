from typing import TypedDict
from core.adapters.controller import Controller
from backoffice.plan.application.commands import AddTodoUseCase


class RequestObject(TypedDict):
    plan_id: str
    description: str


class AddTodoController(Controller[RequestObject]):
    def __init__(self, use_case: AddTodoUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject):
        assert isinstance(request_object["plan_id"], str)
        assert isinstance(request_object["description"], str)
        await self.use_case.interact(
            {
                "plan_id": request_object["plan_id"],
                "description": request_object["description"],
            }
        )
