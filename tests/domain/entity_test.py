import datetime
from core.domain.entities.entity import Entity
from core.domain.entities.value_object import ValueObject


def test_entity_instantiation_no_dates():
    id = ValueObject("123")
    entity = Entity(id)

    assert entity.id.is_equal(id)
    assert isinstance(entity.created_at.value, datetime.datetime)
    assert entity.updated_at is None


def test_entity_instantiation_with_dates():
    id = ValueObject("123")
    created_at = ValueObject(datetime.datetime.now())
    updated_at = ValueObject(datetime.datetime.now())
    entity = Entity(id, created_at, updated_at)

    assert entity.id.is_equal(id)
    assert entity.created_at.is_equal(created_at)
    assert entity.updated_at is not None and entity.updated_at.is_equal(updated_at)
