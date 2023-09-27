from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")


class ValueObject(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def is_equal(self, vo: ValueObject[T]) -> bool:
        return self.value == vo.value
