import asyncio
from core.infrastructure.in_memory_domain_event_bus import InMemoryDomainEventBus
from backoffice.backoffice_context import BackofficeContext
from backoffice.plan.application.subscribers import (
    SendNotificationOnPlanCreatedSubscriber,
    SendNotificationOnPlanCompletedSubscriber,
    SendNotificationOnTodoAddedSubscriber,
)
from backoffice.plan.infrastructure.services import OnScreenNotificationService


async def main():
    # Setup DomainEventBus and Bounded Contexts
    in_memory_domain_event_bus = InMemoryDomainEventBus()
    await in_memory_domain_event_bus.add_subscribers(
        [
            SendNotificationOnPlanCreatedSubscriber(OnScreenNotificationService()),
            SendNotificationOnPlanCompletedSubscriber(OnScreenNotificationService()),
            SendNotificationOnTodoAddedSubscriber(OnScreenNotificationService()),
        ]
    )
    backoffice_context = BackofficeContext(in_memory_domain_event_bus)

    # Run controllers
    await backoffice_context.plan_aggregate.create_plan_controller.execute(
        {
            "name": "My First Plan",
        }
    )
    await backoffice_context.plan_aggregate.find_plans_controller.execute(
        {
            "name": None,
            "limit": 10,
            "offset": 0,
        }
    )
    await backoffice_context.plan_aggregate.add_todo_controller.execute(
        {
            "plan_id": backoffice_context.plan_aggregate.caught_plan_id,
            "description": "My First Todo",
        }
    )
    await backoffice_context.plan_aggregate.update_todo_controller.execute(
        {
            "plan_id": backoffice_context.plan_aggregate.caught_plan_id,
            "todo_id": backoffice_context.plan_aggregate.caught_todo_id,
            "description": "My First Todo (Updated)",
        }
    )
    await backoffice_context.plan_aggregate.check_todo_controller.execute(
        {
            "plan_id": backoffice_context.plan_aggregate.caught_plan_id,
            "todo_id": backoffice_context.plan_aggregate.caught_todo_id,
        }
    )
    await backoffice_context.plan_aggregate.get_plan_controller.execute(
        {
            "id": backoffice_context.plan_aggregate.caught_plan_id,
        }
    )
    await backoffice_context.plan_aggregate.remove_todo_controller.execute(
        {
            "plan_id": backoffice_context.plan_aggregate.caught_plan_id,
            "todo_id": backoffice_context.plan_aggregate.caught_todo_id,
        }
    )


asyncio.run(main())
