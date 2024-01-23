from abc import ABC, abstractmethod
from backoffice.commands.domain.aggregates.create_todo.entities import Todo


class CreateTodoRepository(ABC):
    @abstractmethod
    def generate_id(self) -> str:
        pass

    @abstractmethod
    async def save(self, entity: Todo):
        pass
