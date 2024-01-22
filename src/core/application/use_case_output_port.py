from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class UseCaseOutputPort(ABC, Generic[T]):
    @abstractmethod
    def success(self, response_model: T):
        pass

    @abstractmethod
    def failure(self, error: BaseException):
        pass
