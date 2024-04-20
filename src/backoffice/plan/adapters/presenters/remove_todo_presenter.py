from core.application import UseCaseOutputPort
from backoffice.plan.application.commands import RemoveTodoResponseModel
from backoffice.plan.application.errors import TodoNotRemovedError


class RemoveTodoPresenter(UseCaseOutputPort[RemoveTodoResponseModel]):
    async def success(self, response_model: RemoveTodoResponseModel):
        id = response_model["todo_id"]
        print("===")
        print(f"RemoveTodoPresenter: Todo with ID <{id}> successfully removed.")
        print("===")

    async def failure(self, error: TodoNotRemovedError | Exception):
        print("RemoveTodoPresenter", error)
