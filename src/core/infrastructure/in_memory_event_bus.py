from collections import OrderedDict
from core.domain.events import DomainEvent, DomainEventSubscriber, DomainEventBus


class InMemoryEventBus(DomainEventBus):
    def __init__(self):
        self.subscribers: OrderedDict[str, list[DomainEventSubscriber]] = OrderedDict(
            []
        )

    def publish(self, domain_events: list[DomainEvent]):
        for domain_event in domain_events:
            if domain_event.event_name.value in self.subscribers:
                subscribers = self.subscribers[domain_event.event_name.value]
                for subscriber in subscribers:
                    subscriber.on(domain_event)

    def add_subscribers(self, subscribers: list[DomainEventSubscriber]):
        for subscriber in subscribers:
            subscriber_domain_event_name = subscriber.subscribed_to()
            if subscriber_domain_event_name not in self.subscribers:
                self.subscribers[subscriber_domain_event_name] = []

            self.subscribers[subscriber_domain_event_name].append(subscriber)

    def start(self):
        pass
