from core.application import UseCaseOutputPort
from backoffice.plan.application.commands import UpdateTodoResponseModel
from backoffice.plan.application.errors import TodoNotUpdatedError


class UpdateTodoPresenter(UseCaseOutputPort[UpdateTodoResponseModel]):
    async def success(self, response_model: UpdateTodoResponseModel):
        id = response_model["todo_id"]
        print(f"UpdateTodoPresenter: Todo with ID <{id}> successfully updated.")

    async def failure(self, error: TodoNotUpdatedError | Exception):
        print(error)
