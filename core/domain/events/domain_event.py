from abc import ABC
from core.domain.entities.value_object import ValueObject


class DomainEvent(ABC):
    def __init__(self, event_name: str, aggregate_id: ValueObject[str]):
        self.event_name = event_name
        self.aggregate_id = aggregate_id
