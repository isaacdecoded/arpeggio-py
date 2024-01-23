from core.adapters import View
from backoffice.todo.adapters.presenters import CreateTodoViewModel


class OnScreenCreateTodoView(View[CreateTodoViewModel]):
    async def transform(self, view_model: CreateTodoViewModel):
        id = view_model.get("id")
        error = view_model.get("error")
        if error:
            print(error)

        if id:
            print(f"Todo with id <${id}> successfully created.")
