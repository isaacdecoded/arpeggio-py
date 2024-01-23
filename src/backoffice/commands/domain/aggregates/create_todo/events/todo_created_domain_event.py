import datetime
from core.domain.entities import IdentityObject, DateObject
from core.domain.events import DomainEvent
from backoffice.commands.domain.aggregates.create_todo.value_objects import TodoName


class TodoCreatedDomainEvent(DomainEvent):
    todo_name: str
    todo_created_at: datetime.datetime

    def __init__(
        self, todo_id: IdentityObject, todo_name: TodoName, todo_created_at: DateObject
    ):
        super().__init__(
            TodoCreatedDomainEvent.__name__,
            todo_id.value,
        )
        self.todo_name = todo_name.value
        self.todo_created_at = todo_created_at.value
