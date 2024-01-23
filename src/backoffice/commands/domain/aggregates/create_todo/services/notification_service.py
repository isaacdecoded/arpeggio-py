import datetime
from typing import TypedDict, TypeVar, Generic
from abc import ABC, abstractmethod

RecipientData = TypeVar("RecipientData")


class NotificationRequest(TypedDict, Generic[RecipientData]):
    recipient_data: RecipientData
    todo_id: str | int
    todo_name: str
    todo_created_at: datetime.datetime


class NotificationService(ABC, Generic[RecipientData]):
    @abstractmethod
    async def send_new_todo_details(self, request: NotificationRequest[RecipientData]):
        pass
