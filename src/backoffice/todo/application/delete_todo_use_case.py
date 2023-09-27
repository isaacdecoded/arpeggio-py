from typing import TypedDict
from core.domain.repositories import Criteria, Filter
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.errors import TodosNotDeletedError
from backoffice.todo.domain.repositories import TodoRepository


class DeleteTodoInputData(TypedDict):
    id: str | None


class DeleteTodoOutputData(TypedDict):
    total_deleted: int


class DeleteTodoUseCase(UseCaseInputPort[DeleteTodoInputData]):
    def __init__(
        self,
        todo_repository: TodoRepository,
        output_port: UseCaseOutputPort[DeleteTodoOutputData],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, input_data: DeleteTodoInputData):
        try:
            filters: list[Filter[Todo]] = list()
            id = input_data.get("id")
            if id is not None:
                filters.append(Filter[Todo]("id", "=", id))
            criteria = Criteria[Todo](filters)
            total_deleted = await self.todo_repository.delete(criteria)
            self.output_port.success({"total_deleted": total_deleted})
        except Exception as e:
            self.output_port.failure(TodosNotDeletedError(str(e)))
