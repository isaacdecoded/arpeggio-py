from core.domain.events import DomainEventSubscriber
from backoffice.plan.domain.events import PlanCreatedDomainEvent
from backoffice.plan.domain.services import NotificationService


class SendNotificationOnPlanCreatedSubscriber(
    DomainEventSubscriber[PlanCreatedDomainEvent]
):
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def subscribed_to(self) -> str:
        return PlanCreatedDomainEvent.__name__

    async def on(self, domain_event: PlanCreatedDomainEvent) -> None:
        await self.notification_service.notify_plan_created(
            {
                "plan_id": domain_event.aggregate_root_id,
                "plan_name": domain_event.plan_name,
                "plan_created_at": domain_event.occurring_time,
            }
        )
