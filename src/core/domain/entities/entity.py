import datetime
from abc import ABC
from typing import TypedDict, Optional
from core.domain.entities.identity_object import IdentityObject
from core.domain.entities.date_object import DateObject


class EntityProps(TypedDict):
    id: IdentityObject
    created_at: Optional[DateObject]
    updated_at: Optional[DateObject]


class Entity(ABC):
    id: IdentityObject
    created_at: DateObject
    updated_at: Optional[DateObject]

    def __init__(
        self,
        props: EntityProps,
    ):
        created_at = props.get("created_at")
        self.id = props.get("id")
        self.created_at = (
            created_at
            if created_at is not None
            else DateObject(datetime.datetime.now())
        )
        self.updated_at = props.get("updated_at")
