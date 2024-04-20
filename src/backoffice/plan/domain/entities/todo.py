from typing import TypedDict
from core.domain.models import EntityProps, Entity, IdentityObject, DateObject
from backoffice.plan.domain.value_objects import TodoDescription
from backoffice.plan.domain.enums import TodoStatus


class Props(EntityProps[IdentityObject], TypedDict):
    description: TodoDescription
    status: TodoStatus


class Todo(Entity[IdentityObject]):
    def __init__(self, props: Props):
        super().__init__(props)
        self._description = props.get("description")
        self._status = props.get("status")

    @property
    def description(self):
        return self._description

    @property
    def status(self):
        return self._status

    def change_description(self, description: TodoDescription):
        self._description = description
        self.update(DateObject.now())

    def change_status(self, status: TodoStatus):
        self._status = status
        self.update(DateObject.now())
