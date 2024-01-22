from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Controller(ABC, Generic[T]):
    @abstractmethod
    async def execute(self, request_object: T):
        pass
