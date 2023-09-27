from typing import TypedDict
from core.application import UseCaseOutputPort
from core.adapters import View
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.errors import TodosNotFoundError
from backoffice.todo.application import FindTodosOutputData


class FindTodosViewModel(TypedDict):
    todos: list[Todo] | None
    error: TodosNotFoundError | BaseException | None


class FindTodosPresenter(UseCaseOutputPort[FindTodosOutputData]):
    def __init__(self, view: View[FindTodosViewModel]):
        self.view = view

    def success(self, output_data: FindTodosOutputData):
        self.view.transform(
            {
                "todos": output_data.get("todos"),
                "error": None,
            }
        )

    def failure(self, error: TodosNotFoundError | BaseException):
        self.view.transform(
            {
                "todos": None,
                "error": error,
            }
        )
