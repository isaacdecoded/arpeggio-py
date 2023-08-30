from abc import abstractmethod
from core.domain.events.domain_event import DomainEvent


class DomainEventSubscriber:
    @abstractmethod
    def subscribed_to(self) -> list[str]:
        pass

    @abstractmethod
    def on(self, domain_event: DomainEvent):
        pass
