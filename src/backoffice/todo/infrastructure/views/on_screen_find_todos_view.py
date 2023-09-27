from core.adapters import View
from backoffice.todo.adapters.presenters import FindTodosViewModel


class OnScreenFindTodosView(View[FindTodosViewModel]):
    def transform(self, view_model: FindTodosViewModel):
        todos = view_model.get("todos")
        error = view_model.get("error")
        if error:
            print(error)

        if todos:
            for idx, todo in enumerate(todos):
                print(f"{idx+1}. ${todo.id.value} - ${todo.name.value}")
