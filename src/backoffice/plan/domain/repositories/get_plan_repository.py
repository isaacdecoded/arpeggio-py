from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from core.domain.models import IdentityObject

ReadModel = TypeVar("ReadModel")


class GetPlanRepository(ABC, Generic[ReadModel]):
    @abstractmethod
    async def get_by_id(self, id: IdentityObject) -> ReadModel | None:
        pass
