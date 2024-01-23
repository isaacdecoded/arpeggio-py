import datetime
from typing import TypedDict
from collections import OrderedDict
from core.domain.entities import IdentityObject, DateObject
from backoffice.commands.domain.aggregates.update_todo.entities import Todo
from backoffice.commands.domain.aggregates.update_todo.value_objects import TodoName
from backoffice.commands.domain.aggregates.update_todo.repositories import (
    UpdateTodoRepository,
)


class TodoModel(TypedDict):
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class InMemoryUpdateTodoRepository(UpdateTodoRepository):
    todos: OrderedDict[str | int, TodoModel] = OrderedDict()

    def __init__(self):
        self.todos["MyFirstTodoID"] = {
            "name": "My First Todo",
            "created_at": datetime.datetime.now(),
            "updated_at": None,
        }

    async def get_by_id(self, id: IdentityObject) -> Todo | None:
        todo_model = self.todos.get(id.value)
        return self.to_entity(id.value, todo_model) if todo_model else None

    async def save(self, entity: Todo):
        self.todos[entity.id.value] = {
            "name": entity.name.value,
            "created_at": entity.created_at.value,
            "updated_at": entity.updated_at.value if entity.updated_at else None,
        }

    def to_entity(self, id: str | int, model: TodoModel) -> Todo:
        updated_at = model.get("updated_at")
        return Todo(
            {
                "id": IdentityObject(id),
                "name": TodoName(model.get("name")),
                "created_at": DateObject(model.get("created_at")),
                "updated_at": DateObject(updated_at) if updated_at else None,
            }
        )
