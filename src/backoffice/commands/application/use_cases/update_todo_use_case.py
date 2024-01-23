from typing import TypedDict
from core.domain.entities import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.commands.domain.aggregates.update_todo.value_objects import TodoName
from backoffice.commands.domain.aggregates.update_todo.repositories import (
    UpdateTodoRepository,
)
from backoffice.commands.application.errors import TodoNotUpdatedError


class RequestModel(TypedDict):
    id: str
    name: str


class UpdateTodoResponseModel(TypedDict):
    id: IdentityObject


class UpdateTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        todo_repository: UpdateTodoRepository,
        output_port: UseCaseOutputPort[UpdateTodoResponseModel],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, request_model: RequestModel):
        try:
            id = IdentityObject(request_model.get("id"))
            todo = await self.todo_repository.get_by_id(id)
            if todo is None:
                return await self.output_port.failure(
                    TodoNotUpdatedError(f"Todo with ID <{id.value}> do not exist")
                )
            todo.update_name(TodoName(request_model.get("name")))
            await self.todo_repository.save(todo)
            await self.output_port.success({"id": id})
        except Exception as e:
            await self.output_port.failure(TodoNotUpdatedError(str(e)))
