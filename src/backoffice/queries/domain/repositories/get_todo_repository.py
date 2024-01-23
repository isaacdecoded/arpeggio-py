from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from core.domain.entities import IdentityObject

ReadModel = TypeVar("ReadModel")


class GetTodoRepository(ABC, Generic[ReadModel]):
    @abstractmethod
    async def get_by_id(self, id: IdentityObject) -> ReadModel | None:
        pass
