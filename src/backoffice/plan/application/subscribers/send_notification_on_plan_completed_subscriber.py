from core.domain.events import DomainEventSubscriber
from backoffice.plan.domain.events import PlanCompletedDomainEvent
from backoffice.plan.domain.services import NotificationService


class SendNotificationOnPlanCompletedSubscriber(
    DomainEventSubscriber[PlanCompletedDomainEvent]
):
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def subscribed_to(self) -> str:
        return PlanCompletedDomainEvent.__name__

    async def on(self, domain_event: PlanCompletedDomainEvent) -> None:
        await self.notification_service.notify_plan_completed(
            {
                "plan_id": domain_event.aggregate_root_id,
                "plan_name": domain_event.plan_name,
                "plan_completed_at": domain_event.occurring_time,
            }
        )
