from core.application import UseCaseOutputPort
from backoffice.plan.application.queries import FindPlansResponseModel
from backoffice.plan.application.errors import PlansNotFoundError


class FindPlansPresenter(UseCaseOutputPort[FindPlansResponseModel]):
    async def success(self, response_model: FindPlansResponseModel):
        print("FindPlansPresenter: Found plans:")
        for plan in response_model["plans"]:
            print("Name:", plan["name"])
            print("Todos:", plan["todo_count"])
            print("Created at:", plan["created_at"].isoformat())
            print(
                "Updated at:",
                (plan["updated_at"].isoformat() if plan["updated_at"] else None),
            )

    async def failure(self, error: PlansNotFoundError | Exception):
        print(error)
