from core.adapters import View
from backoffice.todo.adapters.presenters import DeleteTodosViewModel


class OnScreenDeleteTodosView(View[DeleteTodosViewModel]):
    def transform(self, view_model: DeleteTodosViewModel):
        total_deleted = view_model.get("total_deleted")
        error = view_model.get("error")
        if error:
            print(error)

        if total_deleted:
            print(f"Successfully deleted <{total_deleted}> todos.")
