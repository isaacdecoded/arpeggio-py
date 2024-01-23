from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.commands.application.errors import TodoNotCreatedError
from backoffice.commands.application.use_cases import CreateTodoResponseModel


class CreateTodoViewModel(TypedDict):
    id: str | int | None
    error: TodoNotCreatedError | BaseException | None


class CreateTodoPresenter(UseCaseOutputPort[CreateTodoResponseModel]):
    def __init__(self, view: View[CreateTodoViewModel]):
        self.view = view

    async def success(self, response_model: CreateTodoResponseModel):
        id = response_model.get("id")
        await self.view.transform(
            {
                "id": id.value,
                "error": None,
            }
        )

    async def failure(self, error: TodoNotCreatedError | BaseException):
        await self.view.transform(
            {
                "id": None,
                "error": error,
            }
        )
