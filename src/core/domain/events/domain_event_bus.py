from abc import ABC, abstractmethod
from core.domain.events.domain_event import DomainEvent
from core.domain.events.domain_event_subscriber import DomainEventSubscriber


class DomainEventBus(ABC):
    @abstractmethod
    async def publish(self, domain_events: list[DomainEvent]):
        pass

    @abstractmethod
    async def add_subscribers(self, subscribers: list[DomainEventSubscriber]):
        pass
