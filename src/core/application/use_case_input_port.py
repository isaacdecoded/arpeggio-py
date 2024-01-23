from abc import ABC, abstractmethod
from typing import TypeVar, Generic

RequestModel = TypeVar("RequestModel")


class UseCaseInputPort(ABC, Generic[RequestModel]):
    @abstractmethod
    async def interact(self, request_model: RequestModel):
        pass
