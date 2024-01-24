from abc import ABC, abstractmethod
from core.domain.events.domain_event import DomainEvent


class DomainEventSubscriber(ABC):
    @abstractmethod
    def subscribed_to(self) -> str:
        pass

    @abstractmethod
    async def on(self, domain_event: DomainEvent):
        pass
