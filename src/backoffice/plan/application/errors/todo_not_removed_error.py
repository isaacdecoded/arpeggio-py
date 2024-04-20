class TodoNotRemovedError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to remove Todo due to: {msg}")
