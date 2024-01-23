import asyncio
from backoffice.commands.application.use_cases import (
    CreateTodoUseCase,
    UpdateTodoUseCase,
    RemoveTodoUseCase,
)
from backoffice.commands.application.subscribers import (
    SendNotificationOnTodoCreatedSubscriber,
)
from backoffice.queries.application.use_cases import (
    FindTodosUseCase,
    GetTodoUseCase,
)
from backoffice.commands.adapters.controllers import (
    CreateTodoController,
    UpdateTodoController,
    RemoveTodoController,
)
from backoffice.queries.adapters.controllers import (
    FindTodosController,
    GetTodoController,
)
from backoffice.commands.adapters.presenters import (
    CreateTodoPresenter,
    UpdateTodoPresenter,
    RemoveTodoPresenter,
)
from backoffice.queries.adapters.presenters import (
    FindTodosPresenter,
    GetTodoPresenter,
)
from backoffice.commands.infrastructure.repositories import (
    InMemoryCreateTodoRepository,
    InMemoryRemoveTodoRepository,
    InMemoryUpdateTodoRepository,
)
from backoffice.commands.infrastructure.services import OnScreenNotificationService
from backoffice.queries.infrastructure.repositories import (
    InMemoryFindTodosRepository,
    InMemoryGetTodoRepository,
)
from backoffice.commands.infrastructure.views import (
    OnScreenCreateTodoView,
    OnScreenUpdateTodoView,
    OnScreenRemoveTodoView,
)
from backoffice.queries.infrastructure.views import (
    OnScreenFindTodosView,
    OnScreenGetTodoView,
)
from core.infrastructure import InMemoryEventBus


async def main():
    # Setup DomainEventBus and Subscribers
    in_memory_event_bus = InMemoryEventBus()
    await in_memory_event_bus.add_subscribers(
        [
            SendNotificationOnTodoCreatedSubscriber(OnScreenNotificationService()),
        ]
    )

    # Prepare Use Cases
    create_todo_presenter = CreateTodoPresenter(OnScreenCreateTodoView())
    create_todo_use_case = CreateTodoUseCase(
        InMemoryCreateTodoRepository(),
        create_todo_presenter,
        in_memory_event_bus,
    )

    find_todos_presenter = FindTodosPresenter(OnScreenFindTodosView())
    find_todos_use_case = FindTodosUseCase(
        InMemoryFindTodosRepository(),
        find_todos_presenter,
    )

    get_todo_presenter = GetTodoPresenter(OnScreenGetTodoView())
    get_todo_use_case = GetTodoUseCase(
        InMemoryGetTodoRepository(),
        get_todo_presenter,
    )

    update_todo_presenter = UpdateTodoPresenter(OnScreenUpdateTodoView())
    update_todo_use_case = UpdateTodoUseCase(
        InMemoryUpdateTodoRepository(),
        update_todo_presenter,
    )

    remove_todo_presenter = RemoveTodoPresenter(OnScreenRemoveTodoView())
    remove_todo_use_case = RemoveTodoUseCase(
        InMemoryRemoveTodoRepository(),
        remove_todo_presenter,
    )

    # Run controllers
    default_id = "MyFirstTodoID"
    find_todos_controller = FindTodosController(find_todos_use_case)
    await find_todos_controller.execute({"limit": 10, "offset": 0, "name": None})

    create_todo_controller = CreateTodoController(create_todo_use_case)
    await create_todo_controller.execute({"name": "My First Todo"})

    update_todo_controller = UpdateTodoController(update_todo_use_case)
    await update_todo_controller.execute(
        {
            "id": "MyFirstTodoID",
            "name": "My First Todo (Updated)",
        }
    )

    get_todo_controller = GetTodoController(get_todo_use_case)
    await get_todo_controller.execute({"id": default_id})

    remove_todo_controller = RemoveTodoController(remove_todo_use_case)
    await remove_todo_controller.execute({"id": default_id})


asyncio.run(main())
