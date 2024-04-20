from core.application import UseCaseOutputPort
from backoffice.plan.application.queries import GetPlanResponseModel
from backoffice.plan.application.errors import PlanNotFoundError


class GetPlanPresenter(UseCaseOutputPort[GetPlanResponseModel]):
    async def success(self, response_model: GetPlanResponseModel):
        print("GetPlanPresenter: Plan details:")
        print("Name:", response_model["plan"]["name"])
        print("Todos:", response_model["plan"]["todos"])
        print("CreatedAt:", response_model["plan"]["created_at"].isoformat())
        print(
            "UpdatedAt:",
            (
                response_model["plan"]["updated_at"].isoformat()
                if response_model["plan"]["updated_at"]
                else None
            ),
        )

    async def failure(self, error: PlanNotFoundError | Exception):
        print(error)
