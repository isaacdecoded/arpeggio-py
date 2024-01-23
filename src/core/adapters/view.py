from abc import ABC, abstractmethod
from typing import TypeVar, Generic

ViewModel = TypeVar("ViewModel")


class View(ABC, Generic[ViewModel]):
    @abstractmethod
    async def transform(self, view_model: ViewModel):
        pass
