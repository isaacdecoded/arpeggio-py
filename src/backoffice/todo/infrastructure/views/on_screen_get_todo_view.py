from core.adapters import View
from backoffice.todo.adapters.presenters import GetTodoViewModel


class OnScreenGetTodoView(View[GetTodoViewModel]):
    async def transform(self, view_model: GetTodoViewModel):
        todo = view_model.get("todo")
        error = view_model.get("error")
        if error:
            print(error)

        if todo:
            print(f"1. ${todo.id.value} - ${todo.name.value}")
