from core.domain.events import DomainEvent
from backoffice.plan.domain.entities import Plan


class PlanCreatedDomainEvent(DomainEvent):
    def __init__(self, plan: Plan):
        super().__init__(PlanCreatedDomainEvent.__name__, plan.id.value)
        self._plan_name = plan.name.value
        self._plan_created_at = plan.created_at.value

    @property
    def plan_name(self):
        return self._plan_name

    @property
    def plan_created_at(self):
        return self._plan_created_at
