from enum import Enum
from core.domain.entities import ValueObject


class TodoStatuses(Enum):
    ARCHIVED = "ARCHIVED"
    DONE = "DONE"
    REMOVED = "REMOVED"


class TodoStatus(ValueObject[TodoStatuses]):
    def __init__(self, value: TodoStatuses):
        super().__init__(value)
