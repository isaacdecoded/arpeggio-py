from typing import TypedDict
from core.domain.entities import IdentityObject
from core.domain.events import DomainEventBus
from core.application import UseCaseInputPort, UseCaseOutputPort
from backoffice.commands.domain.aggregates.create_todo.entities import Todo
from backoffice.commands.domain.aggregates.create_todo.value_objects import TodoName
from backoffice.commands.domain.aggregates.create_todo.repositories import (
    CreateTodoRepository,
)
from backoffice.commands.application.errors import TodoNotCreatedError


class RequestModel(TypedDict):
    name: str


class CreateTodoResponseModel(TypedDict):
    id: IdentityObject


class CreateTodoUseCase(UseCaseInputPort[RequestModel]):
    def __init__(
        self,
        todo_repository: CreateTodoRepository,
        output_port: UseCaseOutputPort[CreateTodoResponseModel],
        domain_event_bus: DomainEventBus,
    ):
        self.todo_repository = todo_repository
        self.output_port = output_port
        self.domain_event_bus = domain_event_bus

    async def interact(self, request_model: RequestModel):
        try:
            repository_id = self.todo_repository.generate_id()
            id = IdentityObject(repository_id)
            todo = Todo.create(
                {
                    "id": id,
                    "name": TodoName(request_model.get("name")),
                }
            )
            await self.todo_repository.save(todo)
            await self.domain_event_bus.publish(todo.pull_domain_events())
            await self.output_port.success({"id": id})
        except Exception as e:
            await self.output_port.failure(TodoNotCreatedError(str(e)))
