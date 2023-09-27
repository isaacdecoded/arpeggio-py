from core.domain.entities.entity import Entity
from core.domain.events.domain_event import DomainEvent


class AggregateRoot(Entity):
    __domain_events__: list[DomainEvent] = []

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self.__domain_events__.copy()
        self._domain_events = []
        return domain_events

    def add_domain_event(self, domain_event: DomainEvent):
        self.__domain_events__.append(domain_event)
