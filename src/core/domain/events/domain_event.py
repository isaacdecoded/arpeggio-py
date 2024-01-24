import datetime
from abc import ABCMeta


class DomainEvent(metaclass=ABCMeta):
    name: str
    aggregate_root_id: str | int
    occurring_time: datetime.datetime

    def __init__(self, name: str, aggregate_root_id: str | int):
        self.name = name
        self.aggregate_root_id = aggregate_root_id
        self.occurring_time = datetime.datetime.now()
