from core.domain.entities.aggregate_root import AggregateRoot
from core.domain.entities.value_object import ValueObject
from core.domain.events import DomainEvent


def test_aggregate_root_domain_events_pulling():
    id = ValueObject("123")
    aggregate_root = AggregateRoot(id)
    domain_event = DomainEvent("TestDomainEvent", id)
    aggregate_root.record_domain_event(domain_event)
    aggregate_root_domain_events = aggregate_root.pull_domain_events()

    assert len(aggregate_root_domain_events) >= 1
