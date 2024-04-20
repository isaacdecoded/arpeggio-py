class PlanNotFoundError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to fetch Plan due to: {msg}")
