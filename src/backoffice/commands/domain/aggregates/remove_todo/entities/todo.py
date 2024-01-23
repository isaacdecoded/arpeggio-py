import datetime
from typing import TypedDict
from core.domain.entities import EntityProps, AggregateRoot, DateObject
from backoffice.commands.domain.aggregates.remove_todo.value_objects import (
    TodoStatus,
    TodoStatuses,
)


class Props(EntityProps, TypedDict):
    status: TodoStatus


class Todo(AggregateRoot):
    status: TodoStatus

    def __init__(self, props: Props):
        super().__init__(
            {
                "id": props.get("id"),
                "created_at": props.get("created_at"),
                "updated_at": props.get("updated_at"),
            }
        )
        self.status = props.get("status")

    def remove(self):
        self.status = TodoStatus(TodoStatuses.REMOVED)
        self.updated_at = DateObject(datetime.datetime.now())
