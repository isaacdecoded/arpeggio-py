from abc import ABC, abstractmethod
from core.domain.events.domain_event import DomainEvent
from core.domain.events.domain_event_subscriber import DomainEventSubscriber


class DomainEventBus(ABC):
    @abstractmethod
    def publish(self, domain_events: list[DomainEvent]):
        pass

    @abstractmethod
    def add_subscribers(self, subscribers: list[DomainEventSubscriber]):
        pass

    @abstractmethod
    def start(self):
        pass
