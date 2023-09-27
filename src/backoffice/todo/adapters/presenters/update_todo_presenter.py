from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.todo.domain.errors import TodoNotSavedError
from backoffice.todo.application import UpdateTodoOutputData


class UpdateTodoViewModel(TypedDict):
    id: str | None
    error: TodoNotSavedError | BaseException | None


class UpdateTodoPresenter(UseCaseOutputPort[UpdateTodoOutputData]):
    def __init__(self, view: View[UpdateTodoViewModel]):
        self.view = view

    def success(self, output_data: UpdateTodoOutputData):
        id = output_data.get("id")
        self.view.transform(
            {
                "id": id.value,
                "error": None,
            }
        )

    def failure(self, error: TodoNotSavedError | BaseException):
        self.view.transform(
            {
                "id": None,
                "error": error,
            }
        )
