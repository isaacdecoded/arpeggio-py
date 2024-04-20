class TodoNotCheckedError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to check Todo due to: {msg}")
