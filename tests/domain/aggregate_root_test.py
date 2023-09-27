import datetime
from src.core.domain.entities.aggregate_root import AggregateRoot
from src.core.domain.entities.value_object import ValueObject
from src.core.domain.entities.identity_object import IdentityObject
from src.core.domain.entities.date_object import DateObject
from src.core.domain.events import DomainEvent


class TestDomainEvent(DomainEvent):
    __test__ = False

    def __init__(self):
        self.aggregate_id = IdentityObject("id")
        self.occurring_time = DateObject(datetime.datetime.now())
        self.event_name = ValueObject("TestDomainEvent")


def test_aggregate_root_domain_events_pulling():
    id = IdentityObject("123")
    aggregate_root = AggregateRoot(
        {
            "id": id,
            "created_at": None,
            "updated_at": None,
        }
    )
    domain_event = TestDomainEvent()
    aggregate_root.add_domain_event(domain_event)
    aggregate_root_domain_events = aggregate_root.pull_domain_events()

    assert len(aggregate_root_domain_events) >= 1
