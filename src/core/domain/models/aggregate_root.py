from abc import ABC
from typing import TypeVar, Generic
from core.domain.models.entity import Entity
from core.domain.events.domain_event import DomainEvent
from core.domain.models.value_object import ValueObject

Id = TypeVar("Id", bound=ValueObject[str])


class AggregateRoot(Generic[Id], Entity[Id], ABC):
    domain_events: list[DomainEvent] = []

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self.domain_events.copy()
        self.domain_events = []
        return domain_events

    def add_domain_event(self, domain_event: DomainEvent):
        self.domain_events.append(domain_event)
