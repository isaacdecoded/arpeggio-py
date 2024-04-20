from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from core.domain.events.domain_event import DomainEvent

ConcreteDomainEvent = TypeVar("ConcreteDomainEvent", bound=DomainEvent)


class DomainEventSubscriber(ABC, Generic[ConcreteDomainEvent]):
    @abstractmethod
    def subscribed_to(self) -> str:
        pass

    @abstractmethod
    async def on(self, domain_event: ConcreteDomainEvent):
        pass
