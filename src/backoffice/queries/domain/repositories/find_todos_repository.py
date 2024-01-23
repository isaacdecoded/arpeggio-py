from abc import ABC, abstractmethod
from typing import TypeVar, Generic

ReadCriteria = TypeVar("ReadCriteria")
ReadModel = TypeVar("ReadModel")


class FindTodosRepository(ABC, Generic[ReadCriteria, ReadModel]):
    @abstractmethod
    async def find(self, read_criteria: ReadCriteria | None) -> ReadModel:
        pass
