from typing import Tuple, TypedDict, List
from core.domain.models import EntityProps, IdentityObject, AggregateRoot, DateObject
from backoffice.plan.domain.entities.todo import Todo
from backoffice.plan.domain.enums import TodoStatus
from backoffice.plan.domain.value_objects import PlanName, TodoDescription


class Props(EntityProps[IdentityObject], TypedDict):
    name: PlanName
    todos: List[Todo]


class Plan(AggregateRoot[IdentityObject]):
    def __init__(self, props: Props):
        super().__init__(props)
        self._name = props["name"]
        self._todos = props["todos"]

    @property
    def name(self) -> PlanName:
        return self._name

    @property
    def todos(self) -> List[Todo]:
        return self._todos

    @staticmethod
    def create(props: Props) -> "Plan":
        # Circular dependency error workaround
        from backoffice.plan.domain.events import PlanCreatedDomainEvent

        plan = Plan(
            {
                "id": props["id"],
                "name": props["name"],
                "todos": [],
                "created_at": DateObject.now(),
                "updated_at": None,
            }
        )
        plan.add_domain_event(PlanCreatedDomainEvent(plan))
        return plan

    @staticmethod
    def recreate(props: Props) -> "Plan":
        return Plan(props)

    def change_name(self, name: PlanName):
        self._name = name
        self.update(DateObject.now())

    def add_todo(self, id: IdentityObject, description: TodoDescription):
        # Circular dependency error workaround
        from backoffice.plan.domain.events import TodoAddedDomainEvent

        self.validate_description_duplication(description)
        todo = Todo(
            {
                "id": id,
                "description": description,
                "status": TodoStatus.PENDING,
                "created_at": DateObject.now(),
                "updated_at": None,
            }
        )
        self._todos.append(todo)
        self.add_domain_event(TodoAddedDomainEvent(todo))
        self.update(DateObject.now())

    def remove_todo(self, todo_id: IdentityObject):
        if self.is_completed():
            raise Exception("This Plan aggregation's lifecycle is completed")
        idx, todo = self.get_todo(todo_id)
        todo.change_status(TodoStatus.REMOVED)
        self._todos[idx] = todo
        self.update(DateObject.now())

    def change_todo_description(
        self, todo_id: IdentityObject, description: TodoDescription
    ):
        self.validate_description_duplication(description)
        idx, todo = self.get_todo(todo_id)
        todo.change_description(description)
        self._todos[idx] = todo

    def mark_todo_as_done(self, todo_id: IdentityObject):
        idx, todo = self.get_todo(todo_id)
        todo.change_status(TodoStatus.DONE)
        self._todos[idx] = todo
        self.check_completeness()

    def is_completed(self) -> bool:
        return all(todo.status == TodoStatus.DONE for todo in self.todos)

    def check_completeness(self):
        # Circular dependency error workaround
        from backoffice.plan.domain.events import PlanCompletedDomainEvent

        if self.is_completed():
            self.add_domain_event(PlanCompletedDomainEvent(self))

    def validate_description_duplication(self, description: TodoDescription):
        description_already_exist = any(
            todo.description.is_equal(description) for todo in self.todos
        )
        if description_already_exist:
            raise Exception(
                f"Todo with the same description already exist: {description.value}"
            )

    def get_todo(self, todo_id: IdentityObject) -> Tuple[int, Todo]:
        for idx, todo in enumerate(self.todos):
            if todo.id.is_equal(todo_id):
                return idx, todo
        raise Exception(f"Todo not found in current Plan aggregation <{self.id.value}>")
