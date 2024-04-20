from core.domain.models import ValueObject


class PlanName(ValueObject[str]):
    def __init__(self, value: str):
        MAX_LENGTH = 500
        if len(value) > MAX_LENGTH:
            raise ValueError(
                f"The name exceeds the maximum length of {MAX_LENGTH} characters."
            )
        super().__init__(value)
