import datetime
from core.domain.models.value_object import ValueObject


class DateObject(ValueObject[datetime.datetime]):
    @staticmethod
    def now() -> "DateObject":
        return DateObject(datetime.datetime.now())
