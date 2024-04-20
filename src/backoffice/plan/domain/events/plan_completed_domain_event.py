from core.domain.events import DomainEvent
from backoffice.plan.domain.entities import Plan


class PlanCompletedDomainEvent(DomainEvent):
    def __init__(self, plan: Plan):
        super().__init__(PlanCompletedDomainEvent.__name__, plan.id.value)
        self._plan_name = plan.name.value

    @property
    def plan_name(self):
        return self._plan_name
