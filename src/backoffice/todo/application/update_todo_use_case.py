from typing import TypedDict
from core.domain.entities import IdentityObject
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.todo.domain.value_objects import TodoName
from backoffice.todo.domain.errors import TodoNotSavedError
from backoffice.todo.domain.repositories import TodoRepository


class UpdateTodoInputData(TypedDict):
    id: str
    name: str


class UpdateTodoOutputData(TypedDict):
    id: IdentityObject


class UpdateTodoUseCase(UseCaseInputPort[UpdateTodoInputData]):
    def __init__(
        self,
        todo_repository: TodoRepository,
        output_port: UseCaseOutputPort[UpdateTodoOutputData],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, input_data: UpdateTodoInputData):
        id = input_data.get("id")
        try:
            todo_id = IdentityObject(id)
            todo = await self.todo_repository.get_by_id(todo_id)
            if todo:
                todo.update_name(TodoName(input_data.get("name")))
                await self.todo_repository.save(todo)

            self.output_port.success({"id": todo_id})
        except Exception as e:
            self.output_port.failure(TodoNotSavedError(str(e)))
