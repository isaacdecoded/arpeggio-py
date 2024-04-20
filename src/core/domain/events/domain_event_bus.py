from abc import ABC, abstractmethod
from typing import TypeVar, Any
from core.domain.events.domain_event import DomainEvent
from core.domain.events.domain_event_subscriber import DomainEventSubscriber

ConcreteSubscriber = TypeVar("ConcreteSubscriber", bound=DomainEventSubscriber[Any])


class DomainEventBus(ABC):
    @abstractmethod
    async def publish(self, domain_events: list[DomainEvent]):
        pass

    @abstractmethod
    async def add_subscribers(self, subscribers: list[ConcreteSubscriber]):
        pass
