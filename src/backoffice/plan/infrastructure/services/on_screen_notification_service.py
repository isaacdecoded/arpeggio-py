from backoffice.plan.domain.services.notification_service import (
    NotificationService,
    PlanCreatedNotificationRequest,
    PlanCompletedNotificationRequest,
    TodoAddedNotificationRequest,
)


class OnScreenNotificationService(NotificationService):
    async def notify_plan_created(self, request: PlanCreatedNotificationRequest):
        print("===")
        print("OnScreenNotificationService: [Notification] PLAN CREATED:")
        print(
            f"Content: Plan <{request['plan_name']}> has been created at <{request['plan_created_at'].isoformat()}> with ID <{request['plan_id']}>."
        )
        print("===")

    async def notify_plan_completed(self, request: PlanCompletedNotificationRequest):
        print("===")
        print("OnScreenNotificationService: [Notification] PLAN COMPLETED:")
        print(
            f"Content: Plan <{request['plan_name']}> has been completed at <{request['plan_completed_at'].isoformat()}>."
        )
        print("===")

    async def notify_todo_added(self, request: TodoAddedNotificationRequest):
        print("===")
        print("OnScreenNotificationService: [Notification] TODO ADDED:")
        print(
            f"Content: Todo <{request['todo_description']}> has been added at <{request['todo_created_at'].isoformat()}> with ID <{request['todo_id']}>."
        )
        print("===")
