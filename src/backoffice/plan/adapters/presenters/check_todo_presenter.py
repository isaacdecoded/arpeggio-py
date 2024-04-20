from core.application import UseCaseOutputPort
from backoffice.plan.application.commands import CheckTodoResponseModel
from backoffice.plan.application.errors import TodoNotCheckedError


class CheckTodoPresenter(UseCaseOutputPort[CheckTodoResponseModel]):
    async def success(self, response_model: CheckTodoResponseModel):
        id = response_model["todo_id"]
        print(f"CheckTodoPresenter: Todo with ID <{id}> successfully checked.")

    async def failure(self, error: TodoNotCheckedError | Exception):
        print(error)
