import datetime
from abc import ABC
from core.domain.entities.value_object import ValueObject


class Entity(ABC):
    def __init__(
        self,
        id: ValueObject[str],
        created_at: ValueObject[datetime.datetime] | None = None,
        updated_at: ValueObject[datetime.datetime] | None = None,
    ):
        self.id: ValueObject[str] = id
        self.created_at = (
            created_at
            if created_at is not None
            else ValueObject(datetime.datetime.now())
        )
        self.updated_at = updated_at
