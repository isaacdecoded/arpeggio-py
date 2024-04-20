class TodoNotAddedError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to add Todo due to: {msg}")
