class PlanNotCreatedError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"Unable to create Plan due to: {msg}")
