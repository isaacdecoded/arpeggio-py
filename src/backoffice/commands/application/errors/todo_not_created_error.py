class TodoNotCreatedError(BaseException):
    def __init__(self, msg: str):
        super().__init__(f"Unable to create Todo due to: ${msg}")
