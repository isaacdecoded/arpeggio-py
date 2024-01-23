class TodoNotUpdatedError(BaseException):
    def __init__(self, msg: str):
        super().__init__(f"Unable to update Todo due to: {msg}")
