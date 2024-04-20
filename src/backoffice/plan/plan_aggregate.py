from core.domain.events import DomainEventBus
from backoffice.plan.adapters.controllers import (
    CreatePlanController,
    FindPlansController,
    GetPlanController,
    AddTodoController,
    UpdateTodoController,
    RemoveTodoController,
    CheckTodoController,
)
from backoffice.plan.adapters.presenters import (
    AddTodoPresenter,
    CheckTodoPresenter,
    CreatePlanPresenter,
    FindPlansPresenter,
    GetPlanPresenter,
    RemoveTodoPresenter,
    UpdateTodoPresenter,
)
from backoffice.plan.application.commands import (
    CreatePlanUseCase,
    AddTodoUseCase,
    UpdateTodoUseCase,
    RemoveTodoUseCase,
    CheckTodoUseCase,
)
from backoffice.plan.application.queries import FindPlansUseCase, GetPlanUseCase
from backoffice.plan.application.subscribers import (
    SendNotificationOnPlanCreatedSubscriber,
    SendNotificationOnPlanCompletedSubscriber,
    SendNotificationOnTodoAddedSubscriber,
)
from backoffice.plan.infrastructure.repositories import (
    InMemoryFindPlansRepository,
    InMemoryGetPlanRepository,
    InMemoryPlanRepository,
)
from backoffice.plan.infrastructure.services import OnScreenNotificationService


class PlanAggregate:
    def __init__(self, domain_event_bus: DomainEventBus):
        self.caught_plan_id = ""
        self.caught_todo_id = ""

        self.create_plan_controller = CreatePlanController(
            CreatePlanUseCase(
                InMemoryPlanRepository(),
                domain_event_bus,
                CreatePlanPresenter(lambda id: setattr(self, "caught_plan_id", id)),
            )
        )
        self.find_plans_controller = FindPlansController(
            FindPlansUseCase(InMemoryFindPlansRepository(), FindPlansPresenter())
        )
        self.get_plan_controller = GetPlanController(
            GetPlanUseCase(InMemoryGetPlanRepository(), GetPlanPresenter())
        )
        self.add_todo_controller = AddTodoController(
            AddTodoUseCase(
                InMemoryPlanRepository(),
                domain_event_bus,
                AddTodoPresenter(lambda id: setattr(self, "caught_todo_id", id)),
            )
        )
        self.update_todo_controller = UpdateTodoController(
            UpdateTodoUseCase(InMemoryPlanRepository(), UpdateTodoPresenter())
        )
        self.remove_todo_controller = RemoveTodoController(
            RemoveTodoUseCase(InMemoryPlanRepository(), RemoveTodoPresenter())
        )
        self.check_todo_controller = CheckTodoController(
            CheckTodoUseCase(
                InMemoryPlanRepository(), domain_event_bus, CheckTodoPresenter()
            )
        )

    async def prepare(self, domain_event_bus: DomainEventBus):
        await domain_event_bus.add_subscribers(
            [
                SendNotificationOnPlanCreatedSubscriber(OnScreenNotificationService()),
                SendNotificationOnPlanCompletedSubscriber(
                    OnScreenNotificationService()
                ),
                SendNotificationOnTodoAddedSubscriber(OnScreenNotificationService()),
            ]
        )
