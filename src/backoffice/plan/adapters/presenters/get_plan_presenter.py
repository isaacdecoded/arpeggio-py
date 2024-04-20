from core.application import UseCaseOutputPort
from backoffice.plan.application.queries import GetPlanResponseModel
from backoffice.plan.application.errors import PlanNotFoundError


class GetPlanPresenter(UseCaseOutputPort[GetPlanResponseModel]):
    async def success(self, response_model: GetPlanResponseModel):
        todos = [
            {
                "id": str(todo["id"]),
                "status": todo["status"],
                "description": todo["description"],
                "created_at": todo["created_at"].isoformat(),
                "updated_at": (
                    todo["updated_at"].isoformat() if todo["updated_at"] else None
                ),
            }
            for todo in response_model["plan"]["todos"]
        ]
        print("===")
        print("GetPlanPresenter: Plan details:")
        print("Name:", response_model["plan"]["name"])
        print("Todos:", todos)
        print("CreatedAt:", response_model["plan"]["created_at"].isoformat())
        print(
            "UpdatedAt:",
            (
                response_model["plan"]["updated_at"].isoformat()
                if response_model["plan"]["updated_at"]
                else None
            ),
        )
        print("===")

    async def failure(self, error: PlanNotFoundError | Exception):
        print(error)
