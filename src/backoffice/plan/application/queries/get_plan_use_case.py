from typing import TypedDict, Optional
from datetime import datetime
from core.application.use_case_output_port import UseCaseOutputPort
from core.domain.models.identity_object import IdentityObject
from backoffice.plan.domain.repositories import GetPlanRepository
from backoffice.plan.application.errors import PlanNotFoundError


class GetPlanRequestModel(TypedDict):
    id: str


class PlanTodoReadModel(TypedDict):
    id: str
    description: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime]


class GetPlanReadModel(TypedDict):
    name: str
    todos: list[PlanTodoReadModel]
    created_at: datetime
    updated_at: Optional[datetime]


class GetPlanResponseModel(TypedDict):
    plan: GetPlanReadModel


class GetPlanUseCase:
    def __init__(
        self,
        plan_repository: GetPlanRepository[GetPlanReadModel],
        output_port: UseCaseOutputPort[GetPlanResponseModel],
    ):
        self.plan_repository = plan_repository
        self.output_port = output_port

    async def interact(self, request: GetPlanRequestModel):
        try:
            plan = await self.plan_repository.get_by_id(IdentityObject(request["id"]))
            if not plan:
                return await self.output_port.failure(
                    PlanNotFoundError(f"Plan with ID <{request['id']}> doesn't exist")
                )
            await self.output_port.success(GetPlanResponseModel({"plan": plan}))
        except Exception as e:
            await self.output_port.failure(PlanNotFoundError(str(e)))
