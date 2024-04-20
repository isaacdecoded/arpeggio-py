from abc import ABC
import datetime
from typing import Literal

FilterOperator = Literal["=", "!=", ">", "<", "contains", "not_contains"]
SortOrder = Literal["asc", "desc"]


class Filter(ABC):
    def __init__(
        self,
        field: str,
        operator: FilterOperator,
        value: int | str | bool | datetime.datetime,
    ):
        self.field = field
        self.operator = operator
        self.value = value


class Sort:
    def __init__(self, field: str, order: SortOrder):
        self.field = field
        self.order = order


class Criteria(ABC):
    def __init__(
        self,
        filters: list[Filter],
        selection: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: Sort | None = None,
    ):
        self.filters = filters
        self.selection = selection
        self.limit = limit
        self.offset = offset
        self.sort = sort
