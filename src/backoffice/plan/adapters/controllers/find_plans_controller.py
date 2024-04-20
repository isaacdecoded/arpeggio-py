from typing import TypedDict, Optional
from core.adapters.controller import Controller
from backoffice.plan.application.queries import FindPlansUseCase


class RequestObject(TypedDict):
    name: Optional[str]
    limit: int
    offset: int


class FindPlansController(Controller[RequestObject]):
    def __init__(self, use_case: FindPlansUseCase):
        self.use_case = use_case

    async def execute(self, request_object: RequestObject) -> None:
        assert isinstance(request_object["limit"], int)
        assert isinstance(request_object["offset"], int)
        await self.use_case.interact(
            {
                "name": request_object["name"],
                "limit": request_object["limit"],
                "offset": request_object["offset"],
            }
        )
