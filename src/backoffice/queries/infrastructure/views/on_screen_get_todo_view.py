from core.adapters import View
from backoffice.queries.adapters.presenters import GetTodoViewModel


class OnScreenGetTodoView(View[GetTodoViewModel]):
    async def transform(self, view_model: GetTodoViewModel):
        todo = view_model.get("todo")
        error = view_model.get("error")
        if error:
            print(error)

        if todo:
            name = todo.get("name")
            created_at = todo.get("created_at")
            updated_at = todo.get("updated_at")
            print("----------------------")
            print("OnScreenGetTodoView:")
            print(f"\tName: {name}")
            print(f"\tCreatedAt: {created_at}")
            print(f"\tUpdatedAt: {updated_at}")
