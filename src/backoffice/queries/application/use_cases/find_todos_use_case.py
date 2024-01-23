import datetime
from typing import TypedDict
from core.domain.repositories import Criteria, Filter, Sort
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.queries.application.errors import TodosNotFoundError
from backoffice.queries.domain.repositories import FindTodosRepository


class FindTodosRequestModel(TypedDict):
    name: str | None
    offset: int
    limit: int


class FindTodosReadModel(TypedDict):
    id: str
    name: str
    created_at: datetime.datetime


class FindTodosResponseModel(TypedDict):
    todos: list[FindTodosReadModel]


class FindTodosUseCase(UseCaseInputPort[FindTodosRequestModel]):
    def __init__(
        self,
        todo_repository: FindTodosRepository[
            Criteria[FindTodosReadModel], list[FindTodosReadModel]
        ],
        output_port: UseCaseOutputPort[FindTodosResponseModel],
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port

    async def interact(self, request_model: FindTodosRequestModel):
        try:
            criteria: Criteria[FindTodosReadModel] = Criteria[FindTodosReadModel](
                [],
                ["id", "name"],
                request_model.get("limit"),
                request_model.get("offset"),
                Sort("created_at", "desc"),
            )
            name = request_model.get("name")
            if name:
                criteria.filters.append(Filter("name", "contains", name))
            todos = await self.todo_repository.find(criteria)
            await self.output_port.success({"todos": todos})
        except Exception as e:
            await self.output_port.failure(TodosNotFoundError(str(e)))
