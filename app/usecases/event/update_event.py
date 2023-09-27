from app.handler.helper.exceptions import NotFoundException
from app.repository.event import EventRepository
from app.models import Event


class UpdateEventUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, event: Event) -> None:
        existing_event = await self.repository.get_event_by_id(id)
        if not existing_event:
            raise NotFoundException("This event not found")
        event.id = id
        await self.repository.update_event(event)
