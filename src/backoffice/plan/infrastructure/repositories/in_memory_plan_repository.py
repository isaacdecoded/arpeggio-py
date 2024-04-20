from uuid import uuid4
from typing import Optional
from core.domain.models import IdentityObject, DateObject
from backoffice.plan.domain.entities import Plan, Todo
from backoffice.plan.domain.value_objects import PlanName, TodoDescription
from backoffice.plan.domain.repositories.plan_repository import PlanRepository
from backoffice.plan.infrastructure.repositories import (
    InMemoryRepository,
    PlanWriteModel,
    TodoWriteModel,
)


class InMemoryPlanRepository(PlanRepository):
    async def generate_id(self) -> IdentityObject:
        return IdentityObject(str(uuid4()))

    async def get_by_id(self, id: IdentityObject) -> Optional[Plan]:
        plan_model = InMemoryRepository.write_plans.get(id.value)
        if not plan_model:
            return None
        return self.plan_model_to_entity(id.value, plan_model)

    async def save(self, plan: Plan) -> None:
        InMemoryRepository.write_plans[plan.id.value] = self.plan_to_model(plan)
        todo_models = [self.todo_to_model(plan.id, todo) for todo in plan.todos]
        InMemoryRepository.write_todos[plan.id.value] = todo_models
        InMemoryRepository.sync_read_plans(plan)

    def plan_to_model(self, plan: Plan) -> PlanWriteModel:
        return PlanWriteModel(
            {
                "name": plan.name.value,
                "created_at": plan.created_at.value,
                "updated_at": plan.updated_at.value if plan.updated_at else None,
            }
        )

    def todo_to_model(self, planId: IdentityObject, entity: Todo) -> TodoWriteModel:
        return TodoWriteModel(
            id=entity.id.value,
            plan_id=planId.value,
            description=entity.description.value,
            status=entity.status,
            created_at=entity.created_at.value,
            updated_at=entity.updated_at.value if entity.updated_at else None,
        )

    def plan_model_to_entity(self, id: str, model: PlanWriteModel) -> Plan:
        todo_models = InMemoryRepository.write_todos.get(id, [])
        return Plan.recreate(
            {
                "id": IdentityObject(id),
                "name": PlanName(model["name"]),
                "todos": [
                    Todo(
                        {
                            "id": IdentityObject(todo["id"]),
                            "description": TodoDescription(todo["description"]),
                            "status": todo["status"],
                            "created_at": DateObject(todo["created_at"]),
                            "updated_at": (
                                DateObject(todo["updated_at"])
                                if todo["updated_at"]
                                else None
                            ),
                        }
                    )
                    for todo in todo_models
                ],
                "created_at": DateObject(model["created_at"]),
                "updated_at": (
                    DateObject(model["updated_at"]) if model["updated_at"] else None
                ),
            }
        )
