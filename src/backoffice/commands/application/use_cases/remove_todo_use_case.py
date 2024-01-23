from typing import TypedDict
from core.domain.entities import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.commands.domain.aggregates.remove_todo.repositories import (
    RemoveTodoRepository,
)
from backoffice.commands.application.errors import TodoNotRemovedError


class RequestModel(TypedDict):
    id: str


class RemoveTodoResponseModel(TypedDict):
    removed: bool


class RemoveTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        todo_repository: RemoveTodoRepository,
        output_port: UseCaseOutputPort[RemoveTodoResponseModel],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, request_model: RequestModel):
        try:
            id = IdentityObject(request_model.get("id"))
            todo = await self.todo_repository.get_by_id(id)
            if todo is None:
                return await self.output_port.failure(
                    TodoNotRemovedError(f"Todo with ID <{id.value}> do not exist")
                )

            todo.remove()
            await self.output_port.success({"removed": True})
        except Exception as e:
            await self.output_port.failure(TodoNotRemovedError(str(e)))
