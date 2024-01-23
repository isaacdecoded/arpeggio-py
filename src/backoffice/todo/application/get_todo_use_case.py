from typing import TypedDict
from core.domain.entities import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.errors import TodoNotFoundError
from backoffice.todo.domain.repositories import TodoRepository


class GetTodoInputData(TypedDict):
    id: str


class GetTodoOutputData(TypedDict):
    todo: Todo


class GetTodoUseCase(UseCaseInputPort[GetTodoInputData]):
    def __init__(
        self,
        todo_repository: TodoRepository,
        output_port: UseCaseOutputPort[GetTodoOutputData],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, input_data: GetTodoInputData):
        id = input_data.get("id")
        try:
            todo = await self.todo_repository.get_by_id(
                IdentityObject(id),
            )
            if todo is None:
                return await self.output_port.failure(TodoNotFoundError(id))

            await self.output_port.success({"todo": todo})
        except Exception as e:
            await self.output_port.failure(TodoNotFoundError(id, str(e)))
