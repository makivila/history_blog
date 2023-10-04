from app.handler.helper.exceptions import NotFoundException
from app.repository.event import EventRepository
from app.models import Event


class UpdateEventUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, event: Event) -> None:
        old_event = await self.repository.get_event_by_id(id)
        event.id = id
        event.create_dt = old_event.create_dt
        await self.repository.update_event(event)
