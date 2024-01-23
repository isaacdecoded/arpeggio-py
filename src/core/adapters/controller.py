from abc import ABC, abstractmethod
from typing import TypeVar, Generic

RequestObject = TypeVar("RequestObject")


class Controller(ABC, Generic[RequestObject]):
    @abstractmethod
    async def execute(self, request_object: RequestObject):
        pass
