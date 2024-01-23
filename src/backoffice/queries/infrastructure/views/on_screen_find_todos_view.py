from core.adapters import View
from backoffice.queries.adapters.presenters import FindTodosViewModel


class OnScreenFindTodosView(View[FindTodosViewModel]):
    async def transform(self, view_model: FindTodosViewModel):
        todos = view_model.get("todos")
        error = view_model.get("error")
        if error:
            print(error)

        if todos:
            print("----------------------")
            print("OnScreenFindTodosView:")
            for idx, todo in enumerate(todos):
                id = todo.get("id")
                name = todo.get("name")
                created_at = todo.get("created_at")
                print(f"\tTodo {idx+1}. {id} | {name} | {created_at}")
