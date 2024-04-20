from typing import List
from core.domain.repositories import Criteria
from backoffice.plan.domain.repositories import FindPlansRepository
from backoffice.plan.application.queries import FindPlansReadModel
from backoffice.plan.infrastructure.repositories import InMemoryRepository


class InMemoryFindPlansRepository(FindPlansRepository[FindPlansReadModel]):
    async def find(self, criteria: Criteria) -> List[FindPlansReadModel]:
        plans: List[FindPlansReadModel] = []
        for key, value in InMemoryRepository.read_plans.items():
            plans.append(
                FindPlansReadModel(
                    {
                        "id": str(key),
                        "name": value["name"],
                        "todo_count": len(value["todos"]),
                        "created_at": value["created_at"],
                        "updated_at": (
                            value["updated_at"] if value["updated_at"] else None
                        ),
                    }
                )
            )

        filtered_plans: list[FindPlansReadModel] = []
        for p in plans:
            if all(
                f.operator == "=" and getattr(p, f.field) == f.value
                for f in criteria.filters
            ):
                filtered_plans.append(p)
            elif all(
                f.operator == "!=" and getattr(p, f.field) != f.value
                for f in criteria.filters
            ):
                filtered_plans.append(p)
            elif all(
                f.operator == "contains"
                and str(getattr(p, f.field)).__contains__(str(f.value))
                for f in criteria.filters
            ):
                filtered_plans.append(p)
            elif all(
                f.operator == "not_contains"
                and not str(getattr(p, f.field)).__contains__(str(f.value))
                for f in criteria.filters
            ):
                filtered_plans.append(p)

        return filtered_plans
