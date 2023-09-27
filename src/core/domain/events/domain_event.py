from abc import ABC, abstractmethod
from core.domain.entities.value_object import ValueObject
from core.domain.entities.identity_object import IdentityObject
from core.domain.entities.date_object import DateObject


class DomainEvent(ABC):
    aggregate_id: IdentityObject
    event_name: ValueObject[str]
    occurring_time: DateObject

    @abstractmethod
    def __init__(self, aggregate_id: IdentityObject):
        pass
