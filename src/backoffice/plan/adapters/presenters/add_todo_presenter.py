from typing import Callable
from core.application import UseCaseOutputPort
from backoffice.plan.application.commands import AddTodoResponseModel
from backoffice.plan.application.errors import TodoNotAddedError


class AddTodoPresenter(UseCaseOutputPort[AddTodoResponseModel]):
    def __init__(self, todo_id_catcher: Callable[[str], None]):
        self.todo_id_catcher = todo_id_catcher

    async def success(self, response_model: AddTodoResponseModel):
        id = response_model["todo_id"]
        print("===")
        print(f"AddTodoPresenter: Todo with ID <{id}> successfully added.")
        print("===")
        self.todo_id_catcher(id)

    async def failure(self, error: TodoNotAddedError | Exception):
        print(error)
