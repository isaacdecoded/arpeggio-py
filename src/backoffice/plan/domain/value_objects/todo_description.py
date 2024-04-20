from core.domain.models import ValueObject


class TodoDescription(ValueObject[str]):
    def __init__(self, value: str):
        MAX_LENGTH = 1200
        if len(value) > MAX_LENGTH:
            raise ValueError(
                f"The description exceeds the maximum length of {MAX_LENGTH} characters."
            )
        super().__init__(value)
