import datetime
from core.domain.events.domain_event import DomainEvent
from core.domain.entities.entity import Entity
from core.domain.entities.value_object import ValueObject


class AggregateRoot(Entity):
    def __init__(
        self,
        id: ValueObject[str],
        created_at: ValueObject[datetime.datetime] | None = None,
        updated_at: ValueObject[datetime.datetime] | None = None,
    ):
        super().__init__(id, created_at, updated_at)
        self._domain_events: list[DomainEvent] = []

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self._domain_events.copy()
        self._domain_events = []
        return domain_events

    def record_domain_event(self, domain_event: DomainEvent):
        self._domain_events.append(domain_event)
