from core.domain.entities import ValueObject
from core.domain.errors import InvalidArgumentError


class TodoName(ValueObject[str]):
    def __init__(self, value: str):
        if len(value) > 500:
            raise (
                InvalidArgumentError(
                    "The name exceeds the maximum length of 500 characters."
                )
            )
        super().__init__(value)
