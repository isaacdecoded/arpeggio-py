from backoffice.commands.domain.aggregates.create_todo.services import (
    NotificationService,
    NotificationRequest,
)
from backoffice.commands.application.subscribers import EmailRecipientData


class OnScreenNotificationService(NotificationService[EmailRecipientData]):
    async def send_new_todo_details(
        self, request: NotificationRequest[EmailRecipientData]
    ):
        recipient_data_address = request.get("recipient_data").get("address")
        recipient_data_name = request.get("recipient_data").get("name")
        todo_name = request.get("todo_name")
        todo_created_at = request.get("todo_created_at")
        todo_id = request.get("todo_id")
        print("OnScreenNotificationService")
        print(f"\tRecipientAddress: {recipient_data_address}")
        print(f"\tRecipientName: {recipient_data_name}")
        print(
            f"\tContent: `Todo <{todo_name}> has been created at <{todo_created_at}> with ID <{todo_id}>.`"
        )
        pass
