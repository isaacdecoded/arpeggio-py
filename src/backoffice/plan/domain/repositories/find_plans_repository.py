from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from core.domain.repositories.criteria import Criteria

ReadModel = TypeVar("ReadModel")


class FindPlansRepository(ABC, Generic[ReadModel]):
    @abstractmethod
    async def find(self, criteria: Criteria) -> List[ReadModel]:
        pass
