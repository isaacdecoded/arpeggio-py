from typing import TypedDict
from core.domain.events import DomainEventBus
from core.application import UseCaseInputPort, UseCaseOutputPort
from core.domain.models.date_object import DateObject
from backoffice.plan.domain.entities.plan import Plan
from backoffice.plan.domain.value_objects.plan_name import PlanName
from backoffice.plan.domain.repositories.plan_repository import PlanRepository
from backoffice.plan.application.errors import PlanNotCreatedError


class RequestModel(TypedDict):
    name: str


class CreatePlanResponseModel(TypedDict):
    plan_id: str


class CreatePlanUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        plan_repository: PlanRepository,
        domain_event_bus: DomainEventBus,
        output_port: UseCaseOutputPort[CreatePlanResponseModel],
    ):
        self.plan_repository = plan_repository
        self.domain_event_bus = domain_event_bus
        self.output_port = output_port

    async def interact(self, request_model: RequestModel) -> None:
        try:
            id = await self.plan_repository.generate_id()
            plan = Plan.create(
                {
                    "id": id,
                    "name": PlanName(request_model["name"]),
                    "todos": [],
                    "created_at": DateObject.now(),
                    "updated_at": None,
                }
            )
            await self.plan_repository.save(plan)
            await self.domain_event_bus.publish(plan.pull_domain_events())
            await self.output_port.success({"plan_id": id.value})
        except Exception as e:
            await self.output_port.failure(PlanNotCreatedError(str(e)))
