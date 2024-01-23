from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.todo.domain.errors import TodosNotDeletedError
from backoffice.todo.application import DeleteTodoOutputData


class DeleteTodosViewModel(TypedDict):
    total_deleted: int | None
    error: TodosNotDeletedError | BaseException | None


class DeleteTodosPresenter(UseCaseOutputPort[DeleteTodoOutputData]):
    def __init__(self, view: View[DeleteTodosViewModel]):
        self.view = view

    async def success(self, output_data: DeleteTodoOutputData):
        await self.view.transform(
            {
                "total_deleted": output_data.get("total_deleted"),
                "error": None,
            }
        )

    async def failure(self, error: TodosNotDeletedError | BaseException):
        await self.view.transform(
            {
                "total_deleted": None,
                "error": error,
            }
        )
