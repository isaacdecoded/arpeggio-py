import datetime
from core.domain.entities import IdentityObject, DateObject, ValueObject
from core.domain.events import DomainEvent


class TodoCreatedDomainEvent(DomainEvent):
    def __init__(self, aggregate_id: IdentityObject):
        self.aggregate_id = aggregate_id
        self.event_name = ValueObject("TodoCreatedDomainEvent")
        self.occurring_time = DateObject(datetime.datetime.now())
