from typing import TypedDict
from core.domain.models import IdentityObject
from core.domain.events import DomainEventBus
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.plan.domain.repositories import PlanRepository
from backoffice.plan.application.errors import TodoNotCheckedError


class RequestModel(TypedDict):
    plan_id: str
    todo_id: str


class CheckTodoResponseModel(TypedDict):
    todo_id: str


class CheckTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        plan_repository: PlanRepository,
        domain_event_bus: DomainEventBus,
        output_port: UseCaseOutputPort[CheckTodoResponseModel],
    ):
        self.plan_repository = plan_repository
        self.domain_event_bus = domain_event_bus
        self.output_port = output_port

    async def interact(self, request_model: RequestModel):
        try:
            plan_id = request_model["plan_id"]
            todo_id = request_model["todo_id"]
            plan = await self.plan_repository.get_by_id(IdentityObject(plan_id))
            if not plan:
                return await self.output_port.failure(
                    TodoNotCheckedError(f"Plan with ID <{plan_id}> doesn't exist")
                )
            id = IdentityObject(todo_id)
            plan.mark_todo_as_done(id)
            await self.plan_repository.save(plan)
            await self.domain_event_bus.publish(plan.pull_domain_events())
            await self.output_port.success({"todo_id": todo_id})
        except Exception as e:
            await self.output_port.failure(TodoNotCheckedError(str(e)))
