from typing import TypedDict
from core.application import UseCaseInputPort, UseCaseOutputPort
from core.domain.models import IdentityObject
from backoffice.plan.domain.repositories import PlanRepository
from backoffice.plan.application.errors import TodoNotRemovedError


class RequestModel(TypedDict):
    plan_id: str
    todo_id: str


class RemoveTodoResponseModel(TypedDict):
    todo_id: str


class RemoveTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        plan_repository: PlanRepository,
        output_port: UseCaseOutputPort[RemoveTodoResponseModel],
    ):
        self.plan_repository = plan_repository
        self.output_port = output_port

    async def interact(self, request_model: RequestModel) -> None:
        try:
            plan_id = request_model["plan_id"]
            todo_id = request_model["todo_id"]
            plan = await self.plan_repository.get_by_id(IdentityObject(plan_id))
            if not plan:
                return await self.output_port.failure(
                    TodoNotRemovedError(f"Plan with ID <{plan_id}> doesn't exist")
                )
            todo_id_obj = IdentityObject(todo_id)
            plan.remove_todo(todo_id_obj)
            await self.plan_repository.save(plan)
            await self.output_port.success({"todo_id": todo_id})
        except Exception as e:
            await self.output_port.failure(TodoNotRemovedError(str(e)))
