import datetime
from typing import TypedDict
from collections import OrderedDict
from core.domain.repositories import Criteria
from backoffice.queries.application.use_cases.find_todos_use_case import (
    FindTodosReadModel,
)
from backoffice.queries.domain.repositories import FindTodosRepository


class TodoModel(TypedDict):
    name: str
    created_at: datetime.datetime


class InMemoryFindTodosRepository(
    FindTodosRepository[Criteria[FindTodosReadModel], list[FindTodosReadModel]]
):
    todos: OrderedDict[str | int, TodoModel] = OrderedDict()

    def __init__(self):
        self.todos["MyFirstTodoID"] = {
            "name": "My First Todo",
            "created_at": datetime.datetime.now(),
        }

    async def find(
        self, read_criteria: Criteria[FindTodosReadModel] | None
    ) -> list[FindTodosReadModel]:
        # TODO: implement Criteria behaviors
        todos: list[FindTodosReadModel] = []
        for key, value in self.todos.items():
            todos.append(
                {
                    "id": str(key),
                    "name": value.get("name"),
                    "created_at": value.get("created_at"),
                },
            )
        return todos
