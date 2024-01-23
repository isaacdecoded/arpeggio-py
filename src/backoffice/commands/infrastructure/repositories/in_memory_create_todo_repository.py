import datetime
from typing import TypedDict
from collections import OrderedDict
from backoffice.commands.domain.aggregates.create_todo.entities import Todo
from backoffice.commands.domain.aggregates.create_todo.repositories import (
    CreateTodoRepository,
)


class TodoModel(TypedDict):
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class InMemoryCreateTodoRepository(CreateTodoRepository):
    todos: OrderedDict[str | int, TodoModel] = OrderedDict()

    def generate_id(self):
        return "MyFirstTodoID"

    async def save(self, entity: Todo):
        self.todos[entity.id.value] = self.to_model(entity)

    def to_model(self, entity: Todo) -> TodoModel:
        return {
            "name": entity.name.value,
            "created_at": entity.created_at.value,
            "updated_at": entity.updated_at.value if entity.updated_at else None,
        }
