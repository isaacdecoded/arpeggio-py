import datetime
from abc import ABC
from typing import TypedDict, Optional, TypeVar, Generic
from core.domain.models.value_object import ValueObject

Id = TypeVar("Id", bound=ValueObject[str])


class EntityProps(Generic[Id], TypedDict):
    id: Id
    created_at: ValueObject[datetime.datetime]
    updated_at: Optional[ValueObject[datetime.datetime]]


class Entity(ABC, Generic[Id]):
    id: Id
    created_at: ValueObject[datetime.datetime]
    updated_at: Optional[ValueObject[datetime.datetime]]

    def __init__(
        self,
        props: EntityProps[Id],
    ):
        self.id = props.get("id")
        self.created_at = props.get("created_at")
        self.updated_at = props.get("updated_at")

    def update(self, updated_at: ValueObject[datetime.datetime]):
        self.updated_at = updated_at
