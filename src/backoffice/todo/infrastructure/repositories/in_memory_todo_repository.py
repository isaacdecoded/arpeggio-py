import datetime
from typing import TypedDict
from collections import OrderedDict
from core.domain.entities import IdentityObject, DateObject
from core.domain.repositories import Criteria
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.value_objects import TodoName
from backoffice.todo.domain.repositories import TodoRepository


class TodoModel(TypedDict):
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class InMemoryTodoRepository(TodoRepository):
    todos: OrderedDict[str | int, TodoModel] = OrderedDict()

    def generate_id(self):
        return "MyFirstTodoID"

    async def find(self, criteria: Criteria[Todo] | None):
        # TODO: implement Criteria behaviors
        todos: list[Todo] = []
        for key, value in self.todos.items():
            todos.append(
                self.to_entity(
                    key,
                    {
                        "name": value.get("name"),
                        "created_at": value.get("created_at"),
                        "updated_at": value.get("updated_at"),
                    },
                )
            )
        return todos

    async def get_by_id(self, id: IdentityObject) -> Todo | None:
        todo_model = self.todos.get(id.value)
        return self.to_entity(id.value, todo_model) if todo_model else None

    async def save(self, entity: Todo):
        self.todos[entity.id.value] = self.to_model(entity)

    async def delete(self, criteria: Criteria[Todo] | None) -> int:
        # TODO: implement Criteria behaviors
        total_deleted = len(self.todos)
        self.todos.clear()
        return total_deleted

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

    def to_model(self, entity: Todo) -> TodoModel:
        return {
            "name": entity.name.value,
            "created_at": entity.created_at.value,
            "updated_at": entity.updated_at.value if entity.updated_at else None,
        }
