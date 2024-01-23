import datetime
from typing import TypedDict
from core.domain.entities import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.queries.application.errors import TodoNotFoundError
from backoffice.queries.domain.repositories import GetTodoRepository


class GetTodoRequestModel(TypedDict):
    id: str


class GetTodoReadModel(TypedDict):
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class GetTodoResponseModel(TypedDict):
    todo: GetTodoReadModel


class GetTodoUseCase(UseCaseInputPort[GetTodoRequestModel]):
    def __init__(
        self,
        todo_repository: GetTodoRepository[GetTodoReadModel],
        output_port: UseCaseOutputPort[GetTodoResponseModel],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, request_model: GetTodoRequestModel):
        id = request_model.get("id")
        try:
            todo = await self.todo_repository.get_by_id(
                IdentityObject(id),
            )
            if todo is None:
                return await self.output_port.failure(TodoNotFoundError(id))

            await self.output_port.success({"todo": todo})
        except Exception as e:
            await self.output_port.failure(TodoNotFoundError(id, str(e)))
