import datetime
from typing import TypedDict
from core.domain.entities import BaseProps, AggregateRoot, IdentityObject, DateObject
from backoffice.todo.domain.events import TodoCreatedDomainEvent
from backoffice.todo.domain.value_objects import TodoName


class Props(BaseProps, TypedDict):
    name: TodoName


class CreateProps(TypedDict):
    id: IdentityObject
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

    @staticmethod
    def create(props: CreateProps):
        todo = Todo(
            {
                "id": props.get("id"),
                "name": props.get("name"),
                "created_at": None,
                "updated_at": None,
            }
        )
        todo.add_domain_event(TodoCreatedDomainEvent(todo.id))
        return todo

    def update_name(self, name: TodoName):
        self.name = name
        self.updated_at = DateObject(datetime.datetime.now())
