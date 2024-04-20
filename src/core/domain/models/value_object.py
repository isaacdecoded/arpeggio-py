from abc import ABC
from typing import TypeVar, Generic

Value = TypeVar("Value")


class ValueObject(ABC, Generic[Value]):
    def __init__(self, value: Value):
        self.value = value

    def is_equal(self, o: "ValueObject[Value]") -> bool:
        return self.value == o.value
