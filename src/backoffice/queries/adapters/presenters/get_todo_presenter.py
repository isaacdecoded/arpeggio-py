from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.queries.application.errors import TodoNotFoundError
from backoffice.queries.application.use_cases import (
    GetTodoReadModel,
    GetTodoResponseModel,
)


class GetTodoViewModel(TypedDict):
    todo: GetTodoReadModel | None
    error: TodoNotFoundError | BaseException | None


class GetTodoPresenter(UseCaseOutputPort[GetTodoResponseModel]):
    def __init__(self, view: View[GetTodoViewModel]):
        self.view = view

    async def success(self, response_model: GetTodoResponseModel):
        await self.view.transform(
            {
                "todo": response_model.get("todo"),
                "error": None,
            }
        )

    async def failure(self, error: TodoNotFoundError | BaseException):
        await self.view.transform(
            {
                "todo": None,
                "error": error,
            }
        )
