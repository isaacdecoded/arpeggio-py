from typing import List, TypedDict, Optional
from datetime import datetime
from backoffice.plan.domain.entities import Plan
from backoffice.plan.domain.enums import TodoStatus


class TodoWriteModel(TypedDict):
    id: str
    plan_id: str
    description: str
    status: TodoStatus
    created_at: datetime
    updated_at: Optional[datetime]


class PlanWriteModel(TypedDict):
    name: str
    created_at: datetime
    updated_at: Optional[datetime]


class TodoReadModel(TypedDict):
    id: str
    description: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime]


class PlanReadModel(TypedDict):
    id: str
    name: str
    todos: List[TodoReadModel]
    created_at: datetime
    updated_at: Optional[datetime]


class InMemoryRepository:
    read_plans: dict[str, PlanReadModel] = {}
    write_plans: dict[str, PlanWriteModel] = {}
    write_todos: dict[str, list[TodoWriteModel]] = {}

    @staticmethod
    def sync_read_plans(plan: Plan):
        read_plan: PlanReadModel = {
            "id": plan.id.value,
            "name": plan.name.value,
            "todos": [
                TodoReadModel(
                    {
                        "id": todo.id.value,
                        "description": todo.description.value,
                        "status": str(todo.status),
                        "created_at": todo.created_at.value,
                        "updated_at": (
                            todo.updated_at.value
                            if todo.updated_at is not None
                            else None
                        ),
                    }
                )
                for todo in plan.todos
            ],
            "created_at": plan.created_at.value,
            "updated_at": (
                plan.updated_at.value if plan.updated_at is not None else None
            ),
        }
        InMemoryRepository.read_plans[plan.id.value] = read_plan
