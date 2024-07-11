import datetime
from src.core.domain.models import Entity, IdentityObject, DateObject


def test_entity_instantiation_no_dates():
    id = IdentityObject("123")
    date = DateObject(datetime.datetime.now())
    entity = Entity(
        {
            "id": id,
            "created_at": date,
            "updated_at": None,
        }
    )

    assert entity.id.value == id.value
    assert isinstance(entity.created_at.value, datetime.datetime)
    assert entity.updated_at is None


def test_entity_instantiation_with_dates():
    id = IdentityObject("123")
    created_at = DateObject(datetime.datetime.now())
    updated_at = DateObject(datetime.datetime.now())
    entity = Entity(
        {
            "id": id,
            "created_at": created_at,
            "updated_at": updated_at,
        }
    )

    assert entity.id.value == id.value
    assert entity.created_at.value == created_at.value
    assert entity.updated_at is not None and entity.updated_at.value == updated_at.value
