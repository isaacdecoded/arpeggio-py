import asyncio
from backoffice.todo.application import (
    CreateTodoUseCase,
    FindTodosUseCase,
    GetTodoUseCase,
    UpdateTodoUseCase,
    DeleteTodoUseCase,
)
from backoffice.todo.adapters.controllers import (
    CreateTodoController,
    FindTodosController,
    GetTodoController,
    UpdateTodoController,
    DeleteTodosController,
)
from backoffice.todo.adapters.presenters import (
    CreateTodoPresenter,
    FindTodosPresenter,
    GetTodoPresenter,
    UpdateTodoPresenter,
    DeleteTodosPresenter,
)
from backoffice.todo.infrastructure.repositories import InMemoryTodoRepository
from backoffice.todo.infrastructure.views import (
    OnScreenCreateTodoView,
    OnScreenFindTodosView,
    OnScreenGetTodoView,
    OnScreenUpdateTodoView,
    OnScreenDeleteTodosView,
)


async def main():
    from core.infrastructure import (
        InMemoryEventBus,
    )  # lazy loading to prevent circular import

    # Setup implementation components
    in_memory_event_bus = InMemoryEventBus()
    in_memory_todo_repository = InMemoryTodoRepository()
    # await
    in_memory_event_bus.add_subscribers([])  # add required subscribers
    # await
    in_memory_event_bus.start()

    # Prepare Use Cases
    create_todo_presenter = CreateTodoPresenter(OnScreenCreateTodoView())
    create_todo_use_case = CreateTodoUseCase(
        in_memory_todo_repository,
        create_todo_presenter,
        in_memory_event_bus,
    )

    find_todos_presenter = FindTodosPresenter(OnScreenFindTodosView())
    find_todos_use_case = FindTodosUseCase(
        in_memory_todo_repository,
        find_todos_presenter,
    )

    get_todo_presenter = GetTodoPresenter(OnScreenGetTodoView())
    get_todo_use_case = GetTodoUseCase(
        in_memory_todo_repository,
        get_todo_presenter,
    )

    update_todo_presenter = UpdateTodoPresenter(OnScreenUpdateTodoView())
    update_todo_use_case = UpdateTodoUseCase(
        in_memory_todo_repository,
        update_todo_presenter,
    )

    delete_todos_presenter = DeleteTodosPresenter(OnScreenDeleteTodosView())
    delete_todo_use_case = DeleteTodoUseCase(
        in_memory_todo_repository,
        delete_todos_presenter,
    )

    # Run controllers
    create_todo_controller = CreateTodoController(create_todo_use_case)
    await create_todo_controller.execute({"name": "My First Todo"})

    find_todos_controller = FindTodosController(find_todos_use_case)
    await find_todos_controller.execute({"limit": 10, "offset": 0, "name": None})

    update_todo_controller = UpdateTodoController(update_todo_use_case)
    await update_todo_controller.execute(
        {
            "id": "MyFirstTodoID",
            "name": "My First Todo (Updated)",
        }
    )

    get_todo_controller = GetTodoController(get_todo_use_case)
    await get_todo_controller.execute({"id": "MyFirstTodoID"})

    delete_todos_controller = DeleteTodosController(delete_todo_use_case)
    await delete_todos_controller.execute()


asyncio.run(main())
