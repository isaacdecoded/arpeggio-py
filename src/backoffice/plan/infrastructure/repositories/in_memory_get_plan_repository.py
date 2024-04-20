from typing import Optional

from core.domain.models import IdentityObject
from backoffice.plan.domain.repositories import GetPlanRepository
from backoffice.plan.application.queries import GetPlanReadModel, PlanTodoReadModel
from backoffice.plan.infrastructure.repositories import InMemoryRepository


class InMemoryGetPlanRepository(GetPlanRepository[GetPlanReadModel]):
    async def get_by_id(self, id: IdentityObject) -> Optional[GetPlanReadModel]:
        plan_model = InMemoryRepository.read_plans.get(id.value)
        if plan_model:
            return GetPlanReadModel(
                {
                    "name": plan_model["name"],
                    "todos": [
                        PlanTodoReadModel(
                            {
                                "id": str(todo["id"]),
                                "status": todo["status"],
                                "description": todo["description"],
                                "created_at": todo["created_at"],
                                "updated_at": todo["updated_at"],
                            }
                        )
                        for todo in plan_model["todos"]
                    ],
                    "created_at": plan_model["created_at"],
                    "updated_at": (
                        plan_model["updated_at"] if plan_model["updated_at"] else None
                    ),
                }
            )
        return None
