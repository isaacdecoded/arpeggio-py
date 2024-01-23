from core.adapters import View
from backoffice.commands.adapters.presenters import RemoveTodoViewModel


class OnScreenRemoveTodoView(View[RemoveTodoViewModel]):
    async def transform(self, view_model: RemoveTodoViewModel):
        removed = view_model.get("removed")
        error = view_model.get("error")
        if error:
            print(error)

        if removed:
            print("----------------------")
            print("OnScreenRemoveTodoView:")
            print("\tTodo successfully removed")
