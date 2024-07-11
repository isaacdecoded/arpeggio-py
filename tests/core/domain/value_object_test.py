from src.core.domain.models.value_object import ValueObject


def test_value_object_instantiation():
    value = "value"
    value_object = ValueObject(value)

    assert value_object.value is value
