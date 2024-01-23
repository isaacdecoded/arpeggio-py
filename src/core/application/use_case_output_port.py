from abc import ABC, abstractmethod
from typing import TypeVar, Generic

ResponseModel = TypeVar("ResponseModel")


class UseCaseOutputPort(ABC, Generic[ResponseModel]):
    @abstractmethod
    def success(self, response_model: ResponseModel):
        pass

    @abstractmethod
    def failure(self, error: BaseException):
        pass
