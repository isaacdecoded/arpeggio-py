from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class UseCaseInputPort(ABC, Generic[T]):
    @abstractmethod
    async def interact(self, input_data: T):
        pass
