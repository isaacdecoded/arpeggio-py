from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.commands.application.errors import TodoNotRemovedError
from backoffice.commands.application.use_cases import RemoveTodoResponseModel


class RemoveTodoViewModel(TypedDict):
    removed: bool | None
    error: TodoNotRemovedError | BaseException | None


class RemoveTodoPresenter(UseCaseOutputPort[RemoveTodoResponseModel]):
    def __init__(self, view: View[RemoveTodoViewModel]):
        self.view = view

    async def success(self, response_model: RemoveTodoResponseModel):
        await self.view.transform(
            {
                "removed": response_model.get("removed"),
                "error": None,
            }
        )

    async def failure(self, error: TodoNotRemovedError | BaseException):
        await self.view.transform(
            {
                "removed": None,
                "error": error,
            }
        )
