from abc import ABC, abstractmethod
from core.domain.models.identity_object import IdentityObject
from backoffice.plan.domain.entities.plan import Plan


class PlanRepository(ABC):
    @abstractmethod
    async def generate_id(self) -> IdentityObject:
        pass

    @abstractmethod
    async def get_by_id(self, id: IdentityObject) -> Plan | None:
        pass

    @abstractmethod
    async def save(self, plan: Plan):
        pass
