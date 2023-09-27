from abc import ABC, abstractmethod
from core.domain.entities import IdentityObject
from core.domain.repositories import Criteria
from backoffice.todo.domain.entities import Todo


class TodoRepository(ABC):
    @abstractmethod
    def generate_id(self) -> str:
        pass

    @abstractmethod
    async def find(self, criteria: Criteria[Todo] | None) -> list[Todo]:
        pass

    @abstractmethod
    async def get_by_id(self, id: IdentityObject) -> Todo | None:
        pass

    @abstractmethod
    async def save(self, entity: Todo):
        pass

    @abstractmethod
    async def delete(self, criteria: Criteria[Todo] | None) -> int:
        pass
