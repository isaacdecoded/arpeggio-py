from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class View(ABC, Generic[T]):
    @abstractmethod
    def transform(self, view_model: T):
        pass
