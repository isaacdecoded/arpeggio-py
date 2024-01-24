import pytest
import datetime
from src.core.infrastructure.in_memory_event_bus import InMemoryEventBus
from src.core.domain.events import DomainEvent, DomainEventSubscriber


class TestSubscriber(DomainEventSubscriber):
    onCallbackCalled = False

    def subscribed_to(self) -> str:
        return "TestDomainEvent"

    async def on(self, domain_event: DomainEvent):
        self.onCallbackCalled = isinstance(domain_event, TestDomainEvent)


class TestDomainEvent(DomainEvent):
    __test__ = False

    def __init__(self):
        self.name = "TestDomainEvent"
        self.aggregate_root_id = "id"
        self.occurring_time = datetime.datetime.now()


@pytest.mark.asyncio
async def test_in_memory_event_bus_subscription_and_publish():
    in_memory_event_bus = InMemoryEventBus()
    domain_event_subscriber = TestSubscriber()
    domain_event = TestDomainEvent()
    await in_memory_event_bus.add_subscribers([domain_event_subscriber])
    await in_memory_event_bus.publish([domain_event])

    assert len(in_memory_event_bus.subscribers) >= 1
    assert domain_event_subscriber.onCallbackCalled is True
