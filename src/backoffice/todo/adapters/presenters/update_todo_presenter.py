from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.todo.domain.errors import TodoNotSavedError
from backoffice.todo.application import UpdateTodoOutputData


class UpdateTodoViewModel(TypedDict):
    id: str | int | None
    error: TodoNotSavedError | BaseException | None


class UpdateTodoPresenter(UseCaseOutputPort[UpdateTodoOutputData]):
    def __init__(self, view: View[UpdateTodoViewModel]):
        self.view = view

    async def success(self, output_data: UpdateTodoOutputData):
        id = output_data.get("id")
        await self.view.transform(
            {
                "id": id.value,
                "error": None,
            }
        )

    async def failure(self, error: TodoNotSavedError | BaseException):
        await self.view.transform(
            {
                "id": None,
                "error": error,
            }
        )
