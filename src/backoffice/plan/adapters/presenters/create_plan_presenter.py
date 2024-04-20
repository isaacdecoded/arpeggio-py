from typing import Callable
from core.application import UseCaseOutputPort
from backoffice.plan.application.commands import CreatePlanResponseModel
from backoffice.plan.application.errors import PlanNotCreatedError


class CreatePlanPresenter(UseCaseOutputPort[CreatePlanResponseModel]):
    def __init__(self, plan_id_catcher: Callable[[str], None]):
        self.plan_id_catcher = plan_id_catcher

    async def success(self, response_model: CreatePlanResponseModel):
        id = response_model["plan_id"]
        print(f"CreatePlanPresenter: Plan with ID <{id}> successfully added.")
        self.plan_id_catcher(id)

    async def failure(self, error: PlanNotCreatedError | Exception):
        print(error)
