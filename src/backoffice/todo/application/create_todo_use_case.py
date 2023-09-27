from typing import TypedDict
from core.domain.entities import IdentityObject
from core.domain.events import DomainEventBus
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.todo.domain.entities import Todo
from backoffice.todo.domain.value_objects import TodoName
from backoffice.todo.domain.errors import TodoNotSavedError
from backoffice.todo.domain.repositories import TodoRepository


class CreateTodoInputData(TypedDict):
    name: str


class CreateTodoOutputData(TypedDict):
    id: IdentityObject


class CreateTodoUseCase(UseCaseInputPort[CreateTodoInputData]):
    def __init__(
        self,
        todo_repository: TodoRepository,
        output_port: UseCaseOutputPort[CreateTodoOutputData],
        domain_event_bus: DomainEventBus,
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port
        self.domain_event_bus = domain_event_bus

    async def interact(self, input_data: CreateTodoInputData):
        try:
            repository_id = self.todo_repository.generate_id()
            id = IdentityObject(repository_id)
            todo = Todo.create(
                {
                    "id": id,
                    "name": TodoName(input_data.get("name")),
                }
            )
            await self.todo_repository.save(todo)
            self.domain_event_bus.publish(todo.pull_domain_events())
            self.output_port.success({"id": id})
        except Exception as e:
            self.output_port.failure(TodoNotSavedError(str(e)))
