from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.commands.application.errors import TodoNotUpdatedError
from backoffice.commands.application.use_cases import UpdateTodoResponseModel


class UpdateTodoViewModel(TypedDict):
    id: str | int | None
    error: TodoNotUpdatedError | BaseException | None


class UpdateTodoPresenter(UseCaseOutputPort[UpdateTodoResponseModel]):
    def __init__(self, view: View[UpdateTodoViewModel]):
        self.view = view

    async def success(self, response_model: UpdateTodoResponseModel):
        id = response_model.get("id")
        await self.view.transform(
            {
                "id": id.value,
                "error": None,
            }
        )

    async def failure(self, error: TodoNotUpdatedError | BaseException):
        await self.view.transform(
            {
                "id": None,
                "error": error,
            }
        )
