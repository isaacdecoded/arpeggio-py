from typing import TypedDict
from core.domain.models import IdentityObject
from core.domain.events import DomainEventBus
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.plan.domain.value_objects import TodoDescription
from backoffice.plan.domain.repositories import PlanRepository
from backoffice.plan.application.errors import TodoNotAddedError


class RequestModel(TypedDict):
    plan_id: str
    description: str


class AddTodoResponseModel(TypedDict):
    todo_id: str


class AddTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        plan_repository: PlanRepository,
        domain_event_bus: DomainEventBus,
        output_port: UseCaseOutputPort[AddTodoResponseModel],
    ):
        self.plan_repository = plan_repository
        self.domain_event_bus = domain_event_bus
        self.output_port = output_port

    async def interact(self, request_model: RequestModel):
        try:
            plan_id = request_model["plan_id"]
            description = request_model["description"]
            plan = await self.plan_repository.get_by_id(IdentityObject(plan_id))
            if not plan:
                return await self.output_port.failure(
                    TodoNotAddedError(f"Plan with ID <{plan_id}> doesn't exist")
                )
            id = await self.plan_repository.generate_id()
            plan.add_todo(id, TodoDescription(description))
            await self.plan_repository.save(plan)
            await self.domain_event_bus.publish(plan.pull_domain_events())
            await self.output_port.success({"todo_id": id.value})
        except Exception as e:
            await self.output_port.failure(TodoNotAddedError(str(e)))
