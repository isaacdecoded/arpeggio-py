from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from backoffice.plan.domain.repositories.criteria import FindPlansCriteria

ReadModel = TypeVar("ReadModel")


class FindPlansRepository(ABC, Generic[ReadModel]):
    @abstractmethod
    async def find(self, criteria: FindPlansCriteria) -> List[ReadModel]:
        pass
