from abc import abstractmethod
from typing import TypedDict
from datetime import datetime


class PlanCreatedNotificationRequest(TypedDict):
    plan_id: str
    plan_name: str
    plan_created_at: datetime


class PlanCompletedNotificationRequest(TypedDict):
    plan_id: str
    plan_name: str
    plan_completed_at: datetime


class TodoAddedNotificationRequest(TypedDict):
    todo_id: str
    todo_description: str
    todo_created_at: datetime


class NotificationService:
    @abstractmethod
    async def notify_plan_created(self, request: PlanCreatedNotificationRequest):
        pass

    @abstractmethod
    async def notify_plan_completed(self, request: PlanCompletedNotificationRequest):
        pass

    @abstractmethod
    async def notify_todo_added(self, request: TodoAddedNotificationRequest):
        pass
