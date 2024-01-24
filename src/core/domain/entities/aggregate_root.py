from abc import ABC
from core.domain.entities.entity import Entity
from core.domain.events.domain_event import DomainEvent


class AggregateRoot(Entity, ABC):
    domain_events: list[DomainEvent] = []

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self.domain_events.copy()
        self.domain_events = []
        return domain_events

    def add_domain_event(self, domain_event: DomainEvent):
        self.domain_events.append(domain_event)
