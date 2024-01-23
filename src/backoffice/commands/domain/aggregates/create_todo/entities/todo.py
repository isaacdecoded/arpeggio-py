from typing import TypedDict
from core.domain.entities import IdentityObject, AggregateRoot
from backoffice.commands.domain.aggregates.create_todo.events import (
    TodoCreatedDomainEvent,
)
from backoffice.commands.domain.aggregates.create_todo.value_objects import TodoName


class Props(TypedDict):
    id: IdentityObject
    name: TodoName


class Todo(AggregateRoot):
    name: TodoName

    def __init__(self, props: Props):
        super().__init__(
            {
                "id": props.get("id"),
                "created_at": None,
                "updated_at": None,
            }
        )
        self.name = props.get("name")

    @staticmethod
    def create(props: Props):
        todo = Todo(
            {
                "id": props.get("id"),
                "name": props.get("name"),
            }
        )
        todo.add_domain_event(
            TodoCreatedDomainEvent(todo.id, todo.name, todo.created_at)
        )
        return todo
