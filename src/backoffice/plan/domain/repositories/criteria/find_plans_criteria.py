from typing import List, Optional
from enum import Enum
from core.domain.repositories.criteria import Criteria, Filter, Sort


class PlanFieldEnum(Enum):
    NAME = "name"


class FindPlansCriteria(Criteria[PlanFieldEnum]):
    def __init__(
        self,
        filters: List[Filter[PlanFieldEnum]],
        selections: Optional[List[PlanFieldEnum]] = [],
        sorts: Optional[List[Sort[PlanFieldEnum]]] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        self.filters = filters
        self.selections = selections
        self.sorts = sorts
        self.limit = limit
        self.offset = offset
