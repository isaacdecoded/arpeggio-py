class PlansNotFoundError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to fetch Plans due to: {msg}")
