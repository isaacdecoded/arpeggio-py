from collections import OrderedDict
from core.domain.events import DomainEvent, DomainEventSubscriber, DomainEventBus


class InMemoryEventBus(DomainEventBus):
    def __init__(self):
        self.subscribers: OrderedDict[str, list[DomainEventSubscriber]] = OrderedDict(
            []
        )

    async def publish(self, domain_events: list[DomainEvent]):
        for domain_event in domain_events:
            if domain_event.name in self.subscribers:
                subscribers = self.subscribers[domain_event.name]
                for subscriber in subscribers:
                    await subscriber.on(domain_event)

    async def add_subscribers(self, subscribers: list[DomainEventSubscriber]):
        for subscriber in subscribers:
            subscriber_domain_event_name = subscriber.subscribed_to()
            if subscriber_domain_event_name not in self.subscribers:
                self.subscribers[subscriber_domain_event_name] = []

            self.subscribers[subscriber_domain_event_name].append(subscriber)
