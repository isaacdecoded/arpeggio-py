import datetime
from typing import TypedDict
from core.domain.entities import EntityProps, AggregateRoot, DateObject
from backoffice.commands.domain.aggregates.update_todo.value_objects import TodoName


class Props(EntityProps, TypedDict):
    name: TodoName


class Todo(AggregateRoot):
    name: TodoName

    def __init__(self, props: Props):
        super().__init__(
            {
                "id": props.get("id"),
                "created_at": props.get("created_at"),
                "updated_at": props.get("updated_at"),
            }
        )
        self.name = props.get("name")

    def update_name(self, name: TodoName):
        self.name = name
        self.updated_at = DateObject(datetime.datetime.now())
