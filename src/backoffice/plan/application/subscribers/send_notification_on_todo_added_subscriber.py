from core.domain.events import DomainEventSubscriber
from backoffice.plan.domain.events import TodoAddedDomainEvent
from backoffice.plan.domain.services import NotificationService


class SendNotificationOnTodoAddedSubscriber(
    DomainEventSubscriber[TodoAddedDomainEvent]
):
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def subscribed_to(self) -> str:
        return TodoAddedDomainEvent.__name__

    async def on(self, domain_event: TodoAddedDomainEvent) -> None:
        await self.notification_service.notify_todo_added(
            {
                "todo_id": domain_event.aggregate_root_id,
                "todo_description": domain_event.todo_description,
                "todo_created_at": domain_event.todo_created_at,
            }
        )
