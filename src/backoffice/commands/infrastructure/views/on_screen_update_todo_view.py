from core.adapters import View
from backoffice.commands.adapters.presenters import UpdateTodoViewModel


class OnScreenUpdateTodoView(View[UpdateTodoViewModel]):
    async def transform(self, view_model: UpdateTodoViewModel):
        id = view_model.get("id")
        error = view_model.get("error")
        if error:
            print(error)

        if id:
            print("----------------------")
            print("OnScreenUpdateTodoView:")
            print(f"\tTodo with id <{id}> successfully updated")
