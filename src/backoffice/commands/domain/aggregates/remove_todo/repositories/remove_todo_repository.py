from abc import ABC, abstractmethod
from core.domain.entities import IdentityObject
from backoffice.commands.domain.aggregates.remove_todo.entities import Todo


class RemoveTodoRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: IdentityObject) -> Todo | None:
        pass

    @abstractmethod
    async def save(self, entity: Todo):
        pass
