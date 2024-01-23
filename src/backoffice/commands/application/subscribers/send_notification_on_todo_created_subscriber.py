from typing import TypedDict
from core.domain.events import DomainEventSubscriber
from backoffice.commands.domain.aggregates.create_todo.services import (
    NotificationService,
)
from backoffice.commands.domain.aggregates.create_todo.events import (
    TodoCreatedDomainEvent,
)


class EmailRecipientData(TypedDict):
    address: str
    name: str


class SendNotificationOnTodoCreatedSubscriber(DomainEventSubscriber):
    def __init__(
        self,
        notification_service: NotificationService[EmailRecipientData],
    ):
        self.notification_service = notification_service

    def subscribed_to(self) -> str:
        return TodoCreatedDomainEvent.__name__

    # TODO: resume the research to solve this override error from subclass polymorphism
    async def on(self, domain_event: TodoCreatedDomainEvent):
        await self.notification_service.send_new_todo_details(
            {
                "recipient_data": {
                    "address": "arpeggio@arpeggio",
                    "name": "Arpeggio",
                },
                "todo_id": domain_event.aggregate_root_id,
                "todo_name": domain_event.todo_name,
                "todo_created_at": domain_event.todo_created_at,
            },
        )
