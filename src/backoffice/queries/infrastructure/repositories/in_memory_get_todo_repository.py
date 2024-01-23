import datetime
from typing import TypedDict
from collections import OrderedDict
from core.domain.entities import IdentityObject
from backoffice.queries.application.use_cases import GetTodoReadModel
from backoffice.queries.domain.repositories import GetTodoRepository


class TodoModel(TypedDict):
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class InMemoryGetTodoRepository(GetTodoRepository[GetTodoReadModel]):
    todos: OrderedDict[str | int, TodoModel] = OrderedDict()

    def __init__(self):
        self.todos["MyFirstTodoID"] = {
            "name": "My First Todo",
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }

    async def get_by_id(self, id: IdentityObject) -> GetTodoReadModel | None:
        todo_model = self.todos.get(id.value)
        return (
            {
                "name": todo_model.get("name"),
                "created_at": todo_model.get("created_at"),
                "updated_at": todo_model.get("updated_at"),
            }
            if todo_model
            else None
        )
