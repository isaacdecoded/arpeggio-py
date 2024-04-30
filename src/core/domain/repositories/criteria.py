from abc import ABC
import datetime
from typing import Literal, Optional, TypeVar, Generic
from enum import Enum

Enum = TypeVar("Enum", bound=Enum)

FilterOperator = Literal["=", "!=", ">", "<", ">=", "<=", "contains", "not_contains"]
SortOrder = Literal["asc", "desc"]


class Filter(Generic[Enum], ABC):
    def __init__(
        self,
        field: Enum,
        operator: FilterOperator,
        value: int | str | bool | datetime.datetime,
    ):
        self.field = field
        self.operator = operator
        self.value = value


class Sort(Generic[Enum]):
    def __init__(self, field: Enum, order: SortOrder):
        self.field = field
        self.order = order


class Criteria(
    ABC,
    Generic[Enum],
):
    def __init__(
        self,
        filters: list[Filter[Enum]],
        selections: Optional[list[Enum]] = None,
        sorts: Optional[list[Sort[Enum]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        self.filters = filters
        self.selections = selections
        self.sorts = sorts
        self.limit = limit
        self.offset = offset
