from core.domain.events import DomainEvent
from backoffice.plan.domain.entities import Todo


class TodoAddedDomainEvent(DomainEvent):
    def __init__(self, todo: Todo):
        super().__init__(TodoAddedDomainEvent.__name__, todo.id.value)
        self._todo_description = todo.description.value
        self._todo_created_at = todo.created_at.value

    @property
    def todo_description(self):
        return self._todo_description

    @property
    def todo_created_at(self):
        return self._todo_created_at
