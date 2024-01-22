import datetime
from src.core.domain.entities.value_object import ValueObject
from src.core.domain.entities.identity_object import IdentityObject
from src.core.domain.entities.date_object import DateObject
from src.core.infrastructure.in_memory_event_bus import InMemoryEventBus
from src.core.domain.events.domain_event_subscriber import DomainEventSubscriber
from src.core.domain.events.domain_event import DomainEvent


class TestSubscriber(DomainEventSubscriber):
    onCallbackCalled = False

    def subscribed_to(self) -> str:
        return "TestDomainEvent"

    def on(self, domain_event: DomainEvent):
        self.onCallbackCalled = isinstance(domain_event, TestDomainEvent)


class TestDomainEvent(DomainEvent):
    __test__ = False

    def __init__(self):
        self.aggregate_id = IdentityObject("id")
        self.occurring_time = DateObject(datetime.datetime.now())
        self.event_name = ValueObject("TestDomainEvent")


def test_in_memory_event_bus_subscription_and_publish():
    in_memory_event_bus = InMemoryEventBus()
    domain_event_subscriber = TestSubscriber()
    domain_event = TestDomainEvent()
    in_memory_event_bus.add_subscribers([domain_event_subscriber])
    in_memory_event_bus.publish([domain_event])

    assert len(in_memory_event_bus.subscribers) >= 1
    assert domain_event_subscriber.onCallbackCalled is True
