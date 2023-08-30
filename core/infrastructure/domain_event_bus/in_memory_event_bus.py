from collections import OrderedDict
from core.domain.events import DomainEvent, DomainEventSubscriber, DomainEventBus


class InMemoryEventBus(DomainEventBus):
    def __init__(self):
        self.subscriptions: OrderedDict[str, list[DomainEventSubscriber]] = OrderedDict(
            []
        )

    def publish(self, domain_events: list[DomainEvent]):
        for domain_event in domain_events:
            if domain_event.event_name in self.subscriptions:
                subscribers = self.subscriptions[domain_event.event_name]
                for subscriber in subscribers:
                    subscriber.on(domain_event)

    def add_subscribers(self, subscribers: list[DomainEventSubscriber]):
        for subscriber in subscribers:
            print(subscriber.subscribed_to())
            for subscriber_domain_event_name in subscriber.subscribed_to():
                if subscriber_domain_event_name not in self.subscriptions:
                    self.subscriptions[subscriber_domain_event_name] = []

                self.subscriptions[subscriber_domain_event_name].append(subscriber)

    def start(self):
        pass
