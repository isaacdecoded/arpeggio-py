from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.errors import TodoNotFoundError
from backoffice.todo.application import GetTodoOutputData


class GetTodoViewModel(TypedDict):
    todo: Todo | None
    error: TodoNotFoundError | BaseException | None


class GetTodoPresenter(UseCaseOutputPort[GetTodoOutputData]):
    def __init__(self, view: View[GetTodoViewModel]):
        self.view = view

    def success(self, output_data: GetTodoOutputData):
        self.view.transform(
            {
                "todo": output_data.get("todo"),
                "error": None,
            }
        )

    def failure(self, error: TodoNotFoundError | BaseException):
        self.view.transform(
            {
                "todo": None,
                "error": error,
            }
        )
