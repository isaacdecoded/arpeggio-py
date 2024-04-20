from typing import TypedDict
from core.adapters.controller import Controller
from backoffice.plan.application.commands import CreatePlanUseCase


class RequestObject(TypedDict):
    name: str


class CreatePlanController(Controller[RequestObject]):
    def __init__(self, use_case: CreatePlanUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject) -> None:
        assert isinstance(request_object["name"], str)
        await self.use_case.interact({"name": request_object["name"]})
