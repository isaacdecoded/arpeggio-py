from typing import TypedDict
from core.domain.models import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.plan.domain.value_objects import TodoDescription
from backoffice.plan.domain.repositories import PlanRepository
from backoffice.plan.application.errors import TodoNotUpdatedError


class RequestModel(TypedDict):
    plan_id: str
    todo_id: str
    description: str


class UpdateTodoResponseModel(TypedDict):
    todo_id: str


class UpdateTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        plan_repository: PlanRepository,
        output_port: UseCaseOutputPort[UpdateTodoResponseModel],
    ):
        self.plan_repository = plan_repository
        self.output_port = output_port

    async def interact(self, request_model: RequestModel) -> None:
        try:
            plan = await self.plan_repository.get_by_id(
                IdentityObject(request_model["plan_id"])
            )
            if not plan:
                return await self.output_port.failure(
                    TodoNotUpdatedError(
                        f"Plan with ID <{request_model['plan_id']}> doesn't exist"
                    )
                )
            id = IdentityObject(request_model["todo_id"])
            plan.change_todo_description(
                id, TodoDescription(request_model["description"])
            )
            await self.plan_repository.save(plan)
            await self.output_port.success({"todo_id": id.value})
        except Exception as e:
            await self.output_port.failure(TodoNotUpdatedError(str(e)))
