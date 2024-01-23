from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.queries.application.errors import TodosNotFoundError
from backoffice.queries.application.use_cases import (
    FindTodosReadModel,
    FindTodosResponseModel,
)


class FindTodosViewModel(TypedDict):
    todos: list[FindTodosReadModel] | None
    error: TodosNotFoundError | BaseException | None


class FindTodosPresenter(UseCaseOutputPort[FindTodosResponseModel]):
    def __init__(self, view: View[FindTodosViewModel]):
        self.view = view

    async def success(self, response_model: FindTodosResponseModel):
        await self.view.transform(
            {
                "todos": response_model.get("todos"),
                "error": None,
            }
        )

    async def failure(self, error: TodosNotFoundError | BaseException):
        await self.view.transform(
            {
                "todos": None,
                "error": error,
            }
        )
