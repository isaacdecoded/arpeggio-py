from typing import TypedDict
from core.domain.repositories import Criteria, Filter, Sort
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.errors import TodosNotFoundError
from backoffice.todo.domain.repositories import TodoRepository


class FindTodosInputData(TypedDict):
    name: str | None
    offset: int
    limit: int


class FindTodosOutputData(TypedDict):
    todos: list[Todo]


class FindTodosUseCase(UseCaseInputPort[FindTodosInputData]):
    def __init__(
        self,
        todo_repository: TodoRepository,
        output_port: UseCaseOutputPort[FindTodosOutputData],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, input_data: FindTodosInputData):
        try:
            criteria: Criteria[Todo] = Criteria[Todo](
                [],
                ["id", "name"],
                input_data.get("limit"),
                input_data.get("offset"),
                Sort("created_at", "desc"),
            )
            name = input_data.get("name")
            if name:
                criteria.filters.append(Filter("name", "contains", name))
            todos = await self.todo_repository.find(criteria)
            self.output_port.success({"todos": todos})
        except Exception as e:
            self.output_port.failure(TodosNotFoundError(str(e)))
