from typing import Optional, List, TypedDict
from datetime import datetime

from core.application.use_case_output_port import UseCaseOutputPort
from core.domain.repositories.criteria import Filter
from backoffice.plan.domain.repositories import FindPlansRepository
from backoffice.plan.domain.repositories.criteria import (
    FindPlansCriteria,
    PlanFieldEnum,
)
from backoffice.plan.application.errors import PlansNotFoundError


class RequestModel(TypedDict):
    name: Optional[str]
    offset: int
    limit: int


class FindPlansReadModel(TypedDict):
    id: str
    name: str
    todo_count: int
    created_at: datetime
    updated_at: Optional[datetime]


class FindPlansResponseModel(TypedDict):
    plans: List[FindPlansReadModel]


class FindPlansUseCase:
    def __init__(
        self,
        plan_repository: FindPlansRepository[FindPlansReadModel],
        output_port: UseCaseOutputPort[FindPlansResponseModel],
    ):
        self.plan_repository = plan_repository
        self.output_port = output_port

    async def interact(self, request_model: RequestModel) -> None:
        try:
            criteria = FindPlansCriteria(
                filters=[],
                limit=request_model["limit"],
                offset=request_model["offset"],
            )
            if request_model["name"]:
                criteria.filters.append(
                    Filter(PlanFieldEnum.NAME, "contains", request_model["name"])
                )

            plans = await self.plan_repository.find(criteria)
            await self.output_port.success(FindPlansResponseModel({"plans": plans}))
        except Exception as e:
            await self.output_port.failure(PlansNotFoundError(str(e)))
