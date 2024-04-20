import datetime
from abc import ABC


class DomainEvent(ABC):
    name: str
    aggregate_root_id: str
    occurring_time: datetime.datetime

    def __init__(self, name: str, aggregate_root_id: str):
        self.name = name
        self.aggregate_root_id = aggregate_root_id
        self.occurring_time = datetime.datetime.now()
