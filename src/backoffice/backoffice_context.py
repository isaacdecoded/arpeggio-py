from core.domain.events import DomainEventBus
from backoffice.plan.plan_aggregate import PlanAggregate


class BackofficeContext:
    def __init__(self, domain_event_bus: DomainEventBus):
        self.plan_aggregate = PlanAggregate(domain_event_bus)
