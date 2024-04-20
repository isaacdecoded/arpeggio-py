from typing import TypedDict
from core.adapters.controller import Controller
from backoffice.plan.application.queries import GetPlanUseCase


class RequestObject(TypedDict):
    id: str


class GetPlanController(Controller[RequestObject]):
    def __init__(self, use_case: GetPlanUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject) -> None:
        assert isinstance(request_object["id"], str)
        return await self.use_case.interact({"id": request_object["id"]})
